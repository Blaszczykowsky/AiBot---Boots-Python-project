import os
from pathlib import Path

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
        valid_target_dir = os.path.commonpath([target_dir, working_directory_abs]) == working_directory_abs
        if valid_target_dir:
            if os.path.isdir(target_dir):
                return f'Success: "{directory}" is within the working directory'
            else:
                return f'Error: "{directory}" is not a directory'
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"
