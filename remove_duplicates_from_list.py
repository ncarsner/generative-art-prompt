import ast

def remove_duplicates_from_lists(file_path):
    """
    Remove duplicates from all lists in a given Python file and overwrite the file with the updated lists.
    
    Args:
    - file_path (str): The path to the Python file to modify.
    """
    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)

    modified_code = ""

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if isinstance(node.value, ast.List):
                list_variable_name = node.targets[0].id
                list_items = [item.s for item in node.value.elts if isinstance(item, ast.Str)]
                unique_items = list(set(list_items))
                new_list = "[" + ", ".join([f'"{item}"' for item in unique_items]) + "]"
                modified_code += f"{list_variable_name} = {new_list}\n"

    with open(file_path, "w") as file:
        file.write(modified_code)

# Example usage
remove_duplicates_from_lists("words_to_simplify.py")
