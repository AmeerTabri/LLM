from parsing import *
from titles import *

file_num = 1
  
file_path = f"input{file_num}.md"
output_file_path = f"output{file_num}.md"

tree = Tree()
parse_file(file_path, output_file_path, tree)
save_as_html(tree, f"output{file_num}.html")
# tree.print_sections()

tree.tree_to_json() 

import json

def process_json_file(file_path, limit=10): 
    with open(file_path, 'r') as file:
        data = json.load(file)

    i = 0
    for item in data:
        i += 1
        if i == limit:
            break
        item['content'] = item['content'].replace("\n", "").strip()
        section = item.get("section")
        title = item.get("title")
        content = item.get("content")
        
        # Print or process the extracted data
        print(f"Section: {section}")
        print(f"Title: {title}")
        print(f"Content: {content}\n")

        title = generate_title(content)
        tree.add_title(section, title)
        
process_json_file("nodes_without_title.json") 
save_as_html(tree, f"titled_output{file_num}.html")