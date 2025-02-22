from tree import *
import markdown 
import re

# generate all possible subsectins giving a section
def generate_all_subsections(section):
    subsections = [section + ".1"]
    num_dots = section.count('.') 

    for i in range(num_dots): 
        last_dot = section.rfind('.')
        section = section[:last_dot] + "." + str(int(section[last_dot+1:]) + 1)
        subsections.append(section) 
        section = section.rsplit('.', 1)[0]
    for i in range(1,8):
        subsections.append(str(int(section) + i))

    return subsections 

# Checks if the current section follows the correct numbering pattern after the previous section
def is_section_proper(prev_section, curr_section):
    return curr_section in generate_all_subsections(prev_section)
     
# Convert markdown to HTML
def markdown_to_html(markdown_text):
    html_output = markdown.markdown(markdown_text, extensions=['tables'])

    # Add custom CSS for perfect fit column widths
    html_output_with_borders = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Table with Perfect Fit Columns</title>
        <style>
            table {{
                border-collapse: collapse;
                width: auto;
                table-layout: auto; /* Automatically adjust column widths */
            }}
            th, td {{
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                white-space: nowrap; /* Prevent wrapping of text */
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        {html_output}
    </body>
    </html>
    """
    return html_output_with_borders

# Parsing the markdown files and extract sections and subsections from it  
def parse_file(file_path, output_file_path, tree): 
    section_pattern = re.compile(r"^#+\s*(\d+(\.\d+)*)\s*(.*)") 
    prev_section = None
    current_section = None
    start = False

    with open(file_path, "r", encoding="utf-8") as file: 
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            prev_section = ""
            content = "" 
            for line in file: 
                line = line.strip()
                match = section_pattern.match(line)  # Try to match the section pattern
                # New section found
                if match:
                    section = match.group(1)   
                    if not prev_section and section != "1" or prev_section and not is_section_proper(prev_section, section):
                        continue 
                    if prev_section != "":   
                        tree.add_content(prev_section, content)  
                        output_file.write(content) 
                    content = ""
                    start = True
                    prev_section = section
                    title = match.group(3).strip() or "???"
                    current_section = f"# {section} {title}"    
                    tree.add_child(section, title)  # Insert into the tree structure
                    output_file.write(f"{current_section}\n") 
                elif start:
                    content += line + "\n"  # Preserve newlines in the content

            # Add the last section's content
            if prev_section and content:
                section_content = ""
                for line in content: 
                    if line.startswith("#"):
                        break 
                    section_content += line
                # print(prev_section, section_content)  
                tree.add_content(prev_section, section_content) 
                output_file.write(f"{section_content}") 

# Visulization of the file  
def save_as_html(tree, file_name):
    def node_to_html(node, node_id=0):
        # If there's a title, display it in blue and bold, otherwise use "???" in red 
        title = node.title if node.title != "???" else "<span id=\"{node.section}\"; style='color: red;'>???</span>"
        if node.color == "green":
            title = f"<span id=\"{node.section}\"; style='color: green;'>{node.title}</span>"
        elif node.title == "???":
            title = "<span id=\"{node.section}\"; style='color: red;'>???</span>"
        else:
            title = node.title
        title_html = f"<span id=\"{node.section}\"; style='color: blue; font-weight: bold;'>{title}</span>" if node.title else title
        html = f"""
        <li>
            <span style="font-size: 16px; font-weight: bold; color: black; cursor: pointer;" 
                  onclick="toggleContent('content-{node_id}')">
                  {node.section} {title_html}
            </span>
            <div id="content-{node_id}" style="display: none; margin-left: 20px;">
                {f"<p>{markdown_to_html(node.content).strip()}</p>" if markdown_to_html(node.content) else ''}
            </div>
        """
        if node.children:
            html += "<ul>\n"
            for i, child in enumerate(node.children):
                html += node_to_html(child, f"{node_id}-{i}")
            html += "</ul>\n"
        html += "</li>\n"
        return html

    # Open the file 
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Document Structure</title>\n")
        f.write("<style>\n")
        f.write("body { font-family: sans-serif; font-size: 14px; }\n")
        f.write("ul { list-style-type: none; padding-left: 20px; }\n")
        f.write("li { margin-bottom: 10px; }\n")
        f.write("p { margin: 0; padding: 0; }\n")
        f.write("</style>\n")
        f.write("<script>\n")
        f.write("""
        function toggleContent(id) {
            var content = document.getElementById(id);
            if (content.style.display === "none") {
                content.style.display = "block";
            } else {
                content.style.display = "none";
            }
        }

        function toggleAll() {
            var contents = document.querySelectorAll('div[id^="content-"]');
            var toggleState = contents[0].style.display === "none" ? "block" : "none";
            contents.forEach(function(content) {
                content.style.display = toggleState;
            });
        }
        """)
        f.write("</script>\n")
        f.write("</head>\n<body onload=\"toggleAll()\">\n")  # Trigger toggleAll when the page loads

        # Add the button 
        f.write(""" 
        <button onclick="toggleAll()" style="
            position: absolute; 
            top: 10px; 
            right: 10px; 
            width: 40px; 
            height: 40px; 
            background-color: #007BFF; 
            border: none; 
            border-radius: 50%; 
            cursor: pointer; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        ">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 4v16m8-8H4" />
            </svg>
        </button>
        """)

        f.write("<ul>\n  <li>Root\n    <ul>\n")
        for i, child in enumerate(tree.root.children):
            f.write(node_to_html(child, i))
        f.write("    </ul>\n  </li>\n</ul>\n</body>\n</html>")

