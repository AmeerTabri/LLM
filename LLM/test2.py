def add_string_to_section(file_path, search_string, addition_string):
    # Read the original file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Modify lines by adding the string after the search string
    modified_lines = []
    for line in lines:
        if search_string in line:
            print(line)
            # Add the string after the search string
            modified_line = line.replace(search_string, search_string + addition_string)
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)

    # Save the modified lines back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

# Example usage
file_path = 'inputs/input1.md'
search_string = '# 1.5'
addition_string = ' @title' 
add_string_to_section(file_path, search_string, addition_string)
 