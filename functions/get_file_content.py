
import os


def get_file_content(working_directory, file_path):
    
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(abs_working_directory, file_path))
    valid_target_file = os.path.commonpath([abs_working_directory, abs_file_path]) == abs_working_directory
    if not os.path.isfile(abs_file_path):
        return f"Error: File not found or is not a regular file: \"{file_path}\""
    if not valid_target_file:
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory."
    try:
        with open(abs_file_path, 'r') as f:
            content = f.read(10000)  # Read up to 10,000 characters
            if f.read(1):  # Check if there's more content beyond the limit
                content += f"[...File \"{file_path}\" truncated after 10,000 characters...]"
        return content
    except PermissionError:
        return f"Error: Permission denied to read \"{file_path}\"."