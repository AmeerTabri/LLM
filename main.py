from parsing import *
from titles import *
from collections import deque 
import json

file_num = 1

file_path = f"inputs/input{file_num}.md"
output_file_path = f"outputs/output{file_num}.md"

print("k\n")

tree = Tree()
print("k\n")
parse_file(file_path, output_file_path, tree)
save_as_html(tree, f"outputs/output{file_num}.html")
# tree.print_sections()

def process_tree(tree):
    def process_node(node):
        section = node.section
        title = node.title
        content = node.content
        context = tree.parent(node).title

        if title == "???":
            generated_title = generate_title(content, context) 
            tree.add_title(section, generated_title) 

    i = 0
    queue = deque(tree.root.children)  
    while queue:
        node = queue.popleft()    
        if node.title == "???":
            i += 1
            process_node(node)
        if i == 10:
            break
        queue.extend(node.children)


# def process_tree(tree):
#     def process_node(node):
#         section = node.section
#         title = node.title
#         content = node.content
        

#         if title == "???":
#             generated_title = generate_title(content) 
#             tree.add_title(section, generated_title) 

#     queue = deque(tree.root.children)  
#     while queue:
#         node = queue.popleft() 
#         print(f"Section: {node.section}", end = " ") 
#         process_node(node)
#         queue.extend(node.children)


# tree.tree_to_json(empty_cond = True, leaf_cond = False)

# def process_json_file(file_path, limit=15): 
#     with open(file_path, 'r') as file:
#         data = json.load(file)

#     i = 0
#     for item in data:
#         i += 1
#         if i == limit:
#             break
#         item['content'] = item['content'].replace("\n", "").strip()
#         section = item.get("section")
#         title = item.get("title")
#         content = item.get("content")
        
#         # Print or process the extracted data
#         # print(f"Section: {section}")
#         # print(f"Title: {title}")
#         # print(f"Content: {content}\n")

#         parent = tree.ancestor_with_title(tree.find_node(section))
#         parent_title = parent.title
#         print("section = " + section + ", parent section = " + parent.section, ", parent title = " + parent_title)
#         title = generate_title(content, context = parent_title)
#         tree.add_title(section, title)
        
# process_json_file("data_set.json")


# process_tree(tree) 
# save_as_html(tree, f"outputs/large_titled_output{file_num}.html")


tree.tree_to_custom_json()
