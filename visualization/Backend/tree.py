import json 

class Node:
    def __init__(self, value, section="", title="", content="", color = "blue"):
        self.value = value  # The 'value' represents the last digit of the section number, used for searching.
        self.section = section
        self.title = title
        self.content = content
        self.color = color 
        self.children = []

class Tree:
    def __init__(self):
        self.root = Node(0)   

    def add_child(self, section, title = "", content = ""): 
        path = [x for x in section.split('.')]
        color = "red" if (title == "???" or title.isupper()) else ("green" if title[0] == "@" else "white")
        new_node = Node(path[-1], section, title, content, color)
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
        path = section.split('.') 
        
        curr_node = self.root
        for part in path:
            found = False
            for child in curr_node.children:
                if child.value == part: 
                    curr_node = child
                    found = True
                    break
            if not found:
                return None 
             
        return curr_node


    def parent(self, node):
        section = node.section
        if section.count('.') < 1:
            return None
          
        return self.find_node(section[:section.rfind('.')]) 

 
    def add_title(self, section, title):  
        node = self.find_node(section)  
        node.title = title
        node.color = "green"


    def add_content(self, section, content):  
        node = self.find_node(section) 
        if node:
            node.content = content 
 
  
    def print_sections(self):
        def print_section_aux(node, prefix):
            if node:  
                print(prefix + str(node.section) + " " + " " + str(node.title) +  " " + str(node.content))
                for child in node.children:
                    print_section_aux(child, prefix + "    ")

        for child in self.root.children:
            print_section_aux(child, "")
    

    def tree_to_custom_json(self):
        def create_json_node(node):
            json_node = {
                "name": node.section + " " + node.title,
                "fill": self.get_node_fill_color(0 if node == self.root else node.section.count('.') + 1),
                "color": self.get_node_text_color(node.color),
                "isOpen": True if not node.title else False # Initially only the root is open
            }
            
            if node.children:
                json_node["children"] = [create_json_node(child) for child in node.children]
            else:
                json_node["fill"] = "none"
                json_node["stroke"] = self.get_node_fill_color(0 if node == self.root else node.section.count('.') + 1)
                json_node["stroke-width"] = 2
                
            return json_node
         
        root_json = create_json_node(self.root)
         
        with open("Outputs/treeData.json", "w") as f:
            json.dump(root_json, f, indent=2)
 
    
    def get_node_text_color(self, color):
        # making the colors slightly brighter for better visibility 
        if color == 'red':
            return '#FF6347'
        elif color == 'green':
            return '#90EE90'

        return 'white'


    def get_node_fill_color(self, depth): 
        color_map = {
            1: "cyan",
            2: "#32CD32",
            3: "red",
            4: "#FFD700",
        } 
        return color_map.get(depth, "brown")
    
