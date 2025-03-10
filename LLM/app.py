from flask import Flask, request, jsonify
from flask_cors import CORS

from parsing import *
from titles import *
from collections import deque 
import json

app = Flask(__name__)
CORS(app, origins="*")  # Allow all origins to make requests
  
 
trees = {} # Global storage for tree objects
curr_part = 1 # keep track of the selected part

  
# save md file for later use 
def save_md_file(file_path, markdown_data):  
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(markdown_data)
        

# save data file for later use 
def save_data_file(data_file_path, data):
    with open(data_file_path, 'w', encoding="utf-8") as file:
        file.write(data)
        

# process the md file for elements extractions
def process_file(file_path, tree): 
    output_file_path = f"outputs/output.md"
    parse_file(file_path, output_file_path, tree)
    tree.tree_to_custom_json()


# process the data file for elements extractions 
def process_data_file(tree): 
    tree.tree_to_custom_json()


# parsing the data files and extracting its elements 
def extract_elements(file_path):  
    trees.clear()
    doc_name = "" 
    with open(file_path, "r") as file:  
        for line in file:
            line = line.strip()   
            name_pattern = r'name="([^"]+)"' 
            match = re.search(name_pattern, line)
            if match:
                doc_name = match.group(1)  
            
            if line.count(';') == 4:
                elements = line.split(';') 
                pattern = fr"({doc_name})(?:-(\d+))?:(\d{{4}})\s([A-Za-z](?:\.[\d]+)*|[\d.]+)" 
                match = re.search(pattern, elements[2])
                if not match:
                    continue

                part = int(match.group(2)) if match.group(2) else 1
                section = match.group(4)  
                title = elements[3]
                classification = elements[4]
                
                if part not in trees:
                    trees[part] = Tree()
                    
                if section != "0":
                    trees[part].add_child(section=section, title=title, classification=classification)  


# adding titles to the md fileimport  
def add_title_to_section(curr_part, search_section, heading):
    file_path = f"inputs/input{curr_part}.md"

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        # Match the section header (e.g., # section_name)
        if re.match(rf"^#\s*{search_section}", line.strip()):
            print(line)
            # Update the header line by appending the heading
            modified_line = f"# {search_section} @{heading}\n"
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)
 

def collect_sections(node): 
    sections = set() 
    sections.add(node.section)
     
    for child in node.children:
        sections.update(collect_sections(child))
    
    return sections


def collect_empty_sections(root):
    sections = []
    stack = [root]   

    while stack:
        node = stack.pop()

        if node.color in {"red", "green"}:
            sections.append(node.section)

        stack.extend(node.children)   

    return sections[::-1]  # Return the nodes in order


 
def check_equivalence(tree1, tree2):
    def collect_sections(node): 
        sections = set() 
        sections.add(node.section)
        
        for child in node.children:
            sections.update(collect_sections(child))
        
        return sections
 
    tree2_sections = collect_sections(tree2.root)
    
    # Check if all nodes in tree1 is also in tree2
    def check_node_sections(node):
        if node.section not in tree2_sections: 
            return False
        for child in node.children:
            if not check_node_sections(child):
                return False
        return True

    return check_node_sections(tree1.root)


# Analyze the markdown file
@app.route('/markdown', methods=['POST'])
def analyze_markdown():
    try:
        markdown_data = request.data.decode('utf-8') 

        tree = Tree() 
        file_path = f"inputs/input{curr_part}.md"

        save_md_file(file_path, markdown_data)
        process_file(file_path, tree)  

        # Check equivalence
        if not check_equivalence(tree, trees[curr_part]): 
            return jsonify({"incorrect": "Markdown file does not correspond with data file"}), 400

        save_as_html(tree, "outputs/content.html")  

        trees[curr_part] = tree

        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        return jsonify(json_data), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

  
# Analyze the data file
@app.route('/data', methods=['POST'])
def analyze_data():
    try:  
        data = request.data.decode(encoding="utf-8")  

        data_file_path = f"inputs/data.text" 
        save_data_file(data_file_path, data)  
 
        extract_elements(data_file_path)    
        process_data_file(trees[1])
        save_as_html(trees[1], "outputs/content.html")

        num_of_parts = len(trees)

        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        response_data = {
            "num_of_parts": num_of_parts,
            "data": json_data
        }
 
        return jsonify(response_data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Toggle between parts
@app.route('/parts', methods=['POST'])
def change_part():
    try: 
        part_number = request.json.get('part_number') 
        print(f"Selected part: {part_number}")
 
        part_index = int(part_number.replace('part', ''))   

        global curr_part 
        curr_part = part_index 
 
        selected_part = trees[part_index]  
        process_data_file(selected_part)
        save_as_html(selected_part, "outputs/content.html")
 
        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)
 
        return jsonify({"curr_part": curr_part, "data": json_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Generate headings for the tree
@app.route('/headings', methods=['POST'])
def generate_headers():
    try: 
        sections = collect_empty_sections(trees[curr_part].root)
        for section in sections:
            print("generating for ", section)  
    
            node = trees[curr_part].find_node(section)   
            content = node.content
            generated_title = generate_title(content, context="") 
            trees[curr_part].add_title(section, generated_title) 
            add_title_to_section(curr_part, section, generated_title)
 
        trees[curr_part].tree_to_custom_json()
        save_as_html(trees[curr_part], "outputs/content.html") 
         
        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)
    
        return jsonify(json_data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Generate heading for a single node
@app.route('/node_heading', methods=['POST']) 
def generate_node_header():
    try: 
        data = request.get_json() 
        node_section = data.get('node_name')   
 
        elements = node_section.split(' ', 1)
        if len(elements) < 2:
            return jsonify({"error": "Invalid node"}), 400
        
        section = elements[0]
        title = elements[1] 
        
        print("generating for ", section)  
 
        node = trees[curr_part].find_node(section)   
        content = node.content
        generated_title = generate_title(content, context="") 
        trees[curr_part].add_title(section, generated_title)  
        add_title_to_section(curr_part, section, generated_title)

 
        # generated_title = "title"
        # trees[curr_part].add_title(section, generated_title)  
        # add_title_to_section(curr_part, section, generated_title)
          
        trees[curr_part].tree_to_custom_json()
        save_as_html(trees[curr_part], "outputs/content.html") 
 
        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        return jsonify(json_data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
  
if __name__ == "__main__":
    app.run(debug=True)
