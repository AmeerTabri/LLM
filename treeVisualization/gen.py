def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

code_content1 = read_file("code1.txt")
code_content2 = read_file("code2.txt")
input_content = read_file("input.txt")

combined_code = code_content1 + input_content + code_content2

write_file("treeVisual.html", combined_code)
