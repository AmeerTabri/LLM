import re
from tree import *
from parsing import *


def extract_elements(doc): 
    trees = {}
    file_path = fr"C:\Users\Ameer Tabri\Desktop\LLM\standards-atlas-main\data\{doc}" 
    doc_name = ""
    with open(file_path, "r") as file: 
        for line in file:
            line = line.strip()   
            name_pattern = r'name="([^"]+)"' 
            match = re.search(name_pattern, line)
            if match:
                doc_name = match.group(1) 
                print("document name = ", doc_name)
            
            if line.count(';') == 4:
                elements = line.split(';') 
                pattern = fr"({doc_name})(?:-(\d+))?:(\d{{4}})\s([A-Za-z](?:\.[\d]+)*|[\d.]+)" 
                match = re.search(pattern, elements[2])
                if not match:
                    continue

                part = int(match.group(2)) if match.group(2) else 1
                clause = match.group(4)  
                title = elements[3]
                classification = elements[4]
                
                print(str(part) + " " + clause + " " + title + " " + classification)   

                if part not in trees:
                    trees[part] = Tree()

                trees[part].add_child(section=clause, title=title if title != "REQUIREMENT" else "???", classification=classification)  

    return trees


trees = extract_elements(doc = "ISO26262") 
trees[2].print_sections()
# save_as_html(trees[2], "z.html")
print("parts = ", len(trees))
