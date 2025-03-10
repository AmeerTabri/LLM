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
    for i in range(1,8): # allow jumps
        subsections.append(str(int(section) + i))

    return subsections 

# Checks if the current section follows the correct numbering pattern after the previous section
def is_section_proper(prev_section, curr_section):
    return curr_section in generate_all_subsections(prev_section)

 
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
                    content += line + "\n"

            # Add the last section's content
            if prev_section and content:
                section_content = ""
                for line in content: 
                    if line.startswith("#"):
                        break 
                    section_content += line 
                tree.add_content(prev_section, section_content) 
                output_file.write(f"{section_content}") 


# Convert markdown to HTML
def markdown_to_html(markdown_text):
    html_output = markdown.markdown(markdown_text, extensions=['tables']) 
    html_output_with_borders = f"""
        <!DOCTYPE html>
        <html>
        <head> 
            <link rel="stylesheet" type="text/css" href="styles.css">
        </head>
        <body>
            {html_output}
        </body>
        </html>
    """
    return html_output_with_borders
 
# Visulization of the file  
def save_as_html(tree, file_name, curr_part = 1, document_name = "document"):
    def node_to_html(node, node_id=0): 
        title_class = "title blue"
        if node.color == "red":
            title_class = "title red"
        elif node.color == "green":
            title_class = "title green"

        title_html = f'<span class="{title_class}" id="{node.section}">{node.title}</span>'

        html = f"""
        <li>
            <span class="title" onclick="toggleContent('content-{node_id}')">
                {node.section} {title_html}
            </span>
            <div id="content-{node_id}" style="display: none; margin-left: 20px;">
                {f"<p>{markdown_to_html(node.content).strip()}</p>" if node.content else ""}
            </div>
        """

        if node.children:
            html += "<ul>\n"
            for i, child in enumerate(node.children):
                html += node_to_html(child, f"{node_id}-{i}")
            html += "</ul>\n"
        html += "</li>\n"
        return html
 
    doc = f"{document_name}-{curr_part}"
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write("<!DOCTYPE html>\n"
                "<html>\n"
                "<head>\n"
                "    <title> " + str(doc) + "</title>\n"
                "    <link rel='stylesheet' type='text/css' href='styles.css'>\n"
                "    <script>\n"
                "        function toggleContent(id) {\n"
                "            var content = document.getElementById(id);\n"
                "            content.style.display = (content.style.display === 'none') ? 'block' : 'none';\n"
                "        }\n"
                "        function toggleAll() {\n"
                "            var contents = document.querySelectorAll('div[id^=\"content-\"]');\n"
                "            var toggleState = (contents[0].style.display === 'none') ? 'block' : 'none';\n"
                "            contents.forEach(content => content.style.display = toggleState);\n"
                "        }\n"
                "    </script>\n"
                "</head>\n"
                "<body>\n"
                "    <button class='toggle-button' onclick='toggleAll()'>\n"
                "        <svg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'>\n"
                "            <path d='M12 4v16m8-8H4' />\n"
                "        </svg>\n"
                "    </button>\n"
                "    <ul>\n"
                "        <li>Root\n"
                "            <ul>\n")

        for i, child in enumerate(tree.root.children):
            f.write(node_to_html(child, i))

        f.write("""
            </ul>
        </li>
    </ul>
</body>
</html>
""")
