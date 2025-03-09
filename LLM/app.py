from flask import Flask, request, jsonify
from flask_cors import CORS

from parsing import *
from titles import *
from collections import deque 
import json

app = Flask(__name__)
CORS(app, origins="*")  # Allow all origins to make requests

file_num = 1

file_path = f"inputs/input{file_num}.md"
data_file_path = f"inputs/data{file_num}.text"
output_file_path = f"outputs/output{file_num}.md"


trees = {} # Global storage for tree objects
curr_part = 1

def process_tree(tree):
    def process_node(node):
        section = node.section
        title = node.title
        content = node.content
        # context = tree.parent(node).title
         
        if node.color == "red":
            generated_title = generate_title(content)
            tree.add_title(section, generated_title)

    i = 0
    queue = deque(tree.root.children)
    while queue:
        node = queue.popleft()
        print("title " + str(i) + " generated")
        if node.title == "???":
            i += 1
            process_node(node)
        if i == 9:
            break
        queue.extend(node.children)


def save_md_file(markdown_data):
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(markdown_data)
        

def save_data_file(data):
    with open(data_file_path, 'w', encoding="utf-8") as file:
        file.write(data)
        

def process_file(file_path, tree):
    parse_file(file_path, output_file_path, tree)
    tree.tree_to_custom_json()


def process_data_file(tree): 
    tree.tree_to_custom_json()


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
                # print("document name = ", doc_name)
            
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


def collect_sections(node): 
    sections = set() 
    sections.add(node.section)
     
    for child in node.children:
        sections.update(collect_sections(child))
    
    return sections


# check if two trees contains the same nodes
def check_equivalence(tree1, tree2):
    def collect_sections(node): 
        sections = set() 
        sections.add(node.section)
        
        for child in node.children:
            sections.update(collect_sections(child))
        
        return sections
 
    tree2_sections = collect_sections(tree2.root)
    
    # Check if all nodes in tree1 have a section in tree2
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

        print("k")

        save_md_file(markdown_data)
        process_file(file_path, tree) 

        print("kk") 

        # Check equivalence
        if not check_equivalence(tree, trees[curr_part]): 
            return jsonify({"incorrect": "Markdown file does not correspond with data file"}), 400

        save_as_html(tree, "./z.html") 

        print("kkk") 

        trees[curr_part] = tree

        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        # Return the JSON data as a response
        return jsonify(json_data), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

  
# Analyze the data file
@app.route('/data', methods=['POST'])
def analyze_data():
    try:  
        data = request.data.decode(encoding="utf-8")   
        save_data_file(data)  
 
        extract_elements(data_file_path)    
        process_data_file(trees[1])
        save_as_html(trees[1], "./z.html")

        num_of_parts = len(trees)

        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        response_data = {
            "num_of_parts": num_of_parts,
            "data": json_data
        }

        # Return the JSON data as a response 
        return jsonify(response_data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Toggle between parts
@app.route('/parts', methods=['POST'])
def change_part():
    try: 
        part_number = request.json.get('part_number')  # This is a string like "part1" 
        print(f"Selected part: {part_number}")
 
        part_index = int(part_number.replace('part', ''))   

        curr_part = part_index
 
        selected_part = trees[part_index]  
        process_data_file(selected_part)
        save_as_html(selected_part, "./z.html")
 
        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        # Return the selected part data and curr_part as JSON
        return jsonify({"curr_part": curr_part, "data": json_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Generate headings for the tree
@app.route('/headings', methods=['POST'])
def generate_headers():
    try:
        # Retrieve the tree from the global dictionary
        tree = trees[curr_part]
        if not tree:
            return jsonify({"error": "No tree data available"}), 400
  
        process_tree(tree) 
        tree.tree_to_custom_json()
        
        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)
   
        # Return the JSON data as a response
        return jsonify(json_data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Generate heading for a single node
@app.route('/node_heading', methods=['POST'])
def generate_node_header():
    try: 
        data = request.get_json() 
        name = data.get('name') 
        elements = name.split(' ', 1)
        section = elements[0]
        title = elements[1]
        
        print(section + ' ' + title)  

        node = trees[curr_part].find_node(section)  
        content = node.content
        generated_title = generate_title(content, context = "") 
        trees[curr_part].add_title(section, generated_title) 
   
        trees[curr_part].tree_to_custom_json()
        save_as_html(trees[curr_part], "./z.html") 

        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        # Return the JSON data as a response
        return jsonify(json_data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
