from collections import deque
import json

class Node:
    def __init__(self, value, section="", title="", content="", color = "red"):
        self.value = value
        self.section = section
        self.title = title
        self.content = content
        self.color = color
        self.children = []

class Tree:
    def __init__(self):
        self.root = Node(0) 
        self.nodes_without_title = []  # To collect nodes with no title


    def add_child(self, section, title = "", content = ""): 
        path = [int(x) for x in section.split('.')]
        new_node = Node(path[-1], section, title, content)
        curr_node = self.root 
         
        while len(path) > 1: 
            for child in curr_node.children:
                if child.value == path[0]:
                    curr_node = child
                    path.pop(0)
                    break  
            else:
                break  
         
        curr_node.children.append(new_node)

        
    def add_title(self, section, title): 
        path = [int(x) for x in section.split('.')]
         
        curr_node = self.root
        for part in path:
            found = False
            for child in curr_node.children:
                if child.value == part:
                    curr_node = child
                    found = True
                    break
            if not found:
                return  
         
        curr_node.title = title
        curr_node.color = "green"


    def add_content(self, section, content): 
        path = [int(x) for x in section.split('.')]
         
        curr_node = self.root
        for part in path:
            found = False
            for child in curr_node.children:
                if child.value == part:
                    curr_node = child
                    found = True
                    break
            if not found:
                return  
         
        curr_node.content = content

 
    def print_sections(self):
        for child in self.root.children:
            self.print_section_aux(child, "")

    def print_section_aux(self, node, prefix):
        if node:
            # print(prefix + str(node.section))
            print(prefix + str(node.section) + " " + str(node.content))
            for child in node.children:
                self.print_section_aux(child, prefix + "    ")

    
    def tree_to_json(self):
        # Process the entire tree and collect nodes with no title
        for child in self.root.children:
            self.tree_to_json_aux(child)

        # Write the list of nodes with no title to a JSON file
        with open("nodes_without_title.json", "w") as f:
            json.dump(self.nodes_without_title, f, indent=2)

    def tree_to_json_aux(self, node): 
        if not node.title or node.title == '???':
            node_data = {
                "section": node.section,
                "title": node.title,
                "content": node.content
            }
            self.nodes_without_title.append(node_data)

        for child in node.children:
            self.tree_to_json_aux(child)


def read_json_file(file_path):
    try:
        # Open and load the JSON data from the file
        with open(file_path, "r") as file:
            data = json.load(file)

        # Extract and print the content from the JSON data
        for entry in data:
            section = entry.get("section")
            title = entry.get("title")
            content = entry.get("content") 
            # print(f"section: {section}, title: {title}, content: {content}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")


# tree = Tree() 
# tree.add_child("1", "t1")
# tree.add_child("2")
# tree.add_child("3")
# tree.add_child("1.1", "t1.1")
# tree.add_child("1.2")
# tree.add_child("1.2.1")
# tree.add_child("1.2.2")
# tree.add_child("1.2.2")
# tree.add_child("3.2")  

# tree.add_content("1.2.2", "kkk")
# tree.add_content("1", "k")
# tree.add_content("3.2", "kk")

# tree.print_sections()
# tree.tree_to_json() 


# read_json_file("nodes_without_title.json") 

