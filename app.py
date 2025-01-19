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
output_file_path = f"outputs/output{file_num}.md"


def process_tree(tree):
    def process_node(node):
        section = node.section
        title = node.title
        content = node.content
        context = tree.parent(node).title
        print("k1")

        if title == "???":
            generated_title = generate_title(content, context) 
            tree.add_title(section, generated_title) 

    i = 0
    queue = deque(tree.root.children)  
    while queue:
        print("title " + i + " generated")
        node = queue.popleft()    
        if node.title == "???":
            i += 1
            process_node(node)
        if i == 10:
            break
        queue.extend(node.children)


def save_file(markdown_data):
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(markdown_data) 


def process_file(file_path):
    tree = Tree() 
    parse_file(file_path, output_file_path, tree)
    tree.tree_to_custom_json()
    # process_tree(tree)   


@app.route('/analyze', methods=['POST'])
def analyze_markdown():
    try:
        markdown_data = request.data.decode('utf-8')

        save_file(markdown_data)
        process_file(file_path)
  
        json_file_path = "treeVisualization/treeData.json"
        with open(json_file_path, 'r', encoding="utf-8") as json_file:
            json_data = json.load(json_file)  

        # Return the JSON data as a response
        return jsonify(json_data), 200 

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True) 

