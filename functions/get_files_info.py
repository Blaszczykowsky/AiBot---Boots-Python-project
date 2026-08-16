import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
        valid_target_dir = os.path.commonpath([target_dir, working_directory_abs]) == working_directory_abs
        if valid_target_dir:
            if os.path.isdir(target_dir):
                result_list = list()
                for item in os.listdir(target_dir):
                    full_path = os.path.join(target_dir, item)
                    item_str = f"- {item}: file_size={os.path.getsize(full_path)}, is_dir={os.path.isdir(full_path)}"
                    result_list.append(item_str)
                return "\n".join(result_list) 
            else:
                return f'Error: "{directory}" is not a directory'
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

