import json 

class Node:
    def __init__(self, value, section="", title="", content="", color = "blue"):
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
        new_node = Node(path[-1], section, title, content, "red" if title == "???" else "blue")
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


    def find_node(self, section): 
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
                return None  # If no matching child is found, return None
        return curr_node  # Return the node at the given section


    def parent(self, node):
        section = node.section
        if section.count('.') < 1:
            return None
          
        return self.find_node(section[:section.rfind('.')]) 

 
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
        def print_section_aux(node, prefix):
            if node:
                string = prefix + str(node.section) 
                print(f"\033[1m{string}\033[0m", end = "") 
                string = " " + str(node.title)
                print(f"\033[32m{string}\033[0m", end = "") 
                string = " " + str(node.content)
                print(f"\033[36m{string}\033[0m")  
                for child in node.children:
                    print_section_aux(child, prefix + "    ")

        for child in self.root.children:
            print_section_aux(child, "")
    

    def tree_to_json(self, empty_cond = True, leaf_cond = False):
        def tree_to_json_aux(node, empty_cond, leaf_cond): 
            is_empty = not node.title or node.title == '???'
            is_leaf = not node.children
            
            if empty_cond == is_empty and (leaf_cond == is_leaf or leaf_cond == False):
                node_data = {
                    "section": node.section,
                    "title": node.title,
                    "content": node.content
                }
                self.nodes_without_title.append(node_data)
                # print(node.section)

            for child in node.children:
                tree_to_json_aux(child, empty_cond, leaf_cond)

        # Process the entire tree and collect nodes with no title
        for child in self.root.children:
            tree_to_json_aux(child, empty_cond, leaf_cond)

        # Write the list of nodes with no title to a JSON file
        with open("data_set.json", "w") as f:
            json.dump(self.nodes_without_title, f, indent=2)


    def tree_to_custom_json(self):
        def create_json_node(node):
            json_node = {
                "name": node.section + (") " if not node == self.root else "") + node.title,
                "fill": self.get_node_fill_color(0 if node == self.root else node.section.count('.') + 1),
                # "fill": node.color,
                "color": node.color
            }
            
            if node.children:
                json_node["children"] = [create_json_node(child) for child in node.children]
            else:
                json_node["fill"] = "none"
                json_node["stroke"] = self.get_node_fill_color(0 if node == self.root else node.section.count('.') + 1)
                json_node["stroke-width"] = 2
                
            return json_node
        
        # Start from the root node and build the JSON structure
        root_json = create_json_node(self.root)
        
        # Output the final JSON to a file
        with open("treeVisualization/treeData.json", "w") as f:
            json.dump(root_json, f, indent=2)


    def get_node_fill_color(self, depth): 
        color_map = {
            1: "cyan",
            2: "#32CD32",
            3: "red",
            4: "#FFD700",
        }
        # color_map = {}
        return color_map.get(depth, "brown")


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
# tree.add_child("1", "t")
# tree.add_child("2")
# tree.add_child("3")
# tree.add_child("1.1", "tt")
# tree.add_child("1.2", "tt")
# tree.add_child("1.3")
# tree.add_child("1.4")
# tree.add_child("1.2.1")
# tree.add_child("1.2.2")
# tree.add_child("1.2.2")
# tree.add_child("3.2")  

# tree.add_content("1.2.2", "ccc")
# tree.add_content("1", "c")
# tree.add_content("3.2", "cc")

# tree.print_sections()

# print(tree.find_node("1.2.2").section)
# print(tree.parent(tree.find_node("1.2.2")).section)  
# tree.tree_to_json() 


# read_json_file("nodes_without_title.json") 


# tree = Tree()
# tree.add_child("1", "Title 1")
# tree.add_child("1.1", "Title 1.1")
# tree.add_child("1.2", "Title 1.2")
# tree.add_child("1.2.1", "Title 1.2.1")
# tree.add_child("2", "Title 2")
# tree.add_child("2.1", "Title 2.1")
# tree.add_child("3", "Title 3")
# tree.add_child("3.1", "Title 3.1")
# tree.add_child("3.2", "Title 3.2")
# tree.add_child("4", "Title 4")

# # Generate and save the custom JSON
# tree.tree_to_custom_json()