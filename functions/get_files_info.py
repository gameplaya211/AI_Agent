import os
def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.normpath(os.path.join(abs_working_directory, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([abs_working_directory, abs_directory]) == abs_working_directory
    if not valid_target_dir:
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    if not os.path.isdir(abs_directory):
        return f"Error: \"{directory}\" is not a directory"
    try:
        result = []
        for entry in os.listdir(abs_directory):
            entry_path = os.path.join(abs_directory, entry)
            size = os.path.getsize(entry_path)
            if os.path.isfile(entry_path):
                
                result.append(f"- {entry}: file_size={size} bytes, is_dir=False")
            elif os.path.isdir(entry_path):
                result.append(f"- {entry}: file_size={size} bytes, is_dir=True")
    except PermissionError:
        return f"Error: Permission denied to access \"{directory}\"."
    return "\n".join(result)
