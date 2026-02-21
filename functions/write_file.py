import os
from google.genai import types
def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(abs_working_directory, file_path))
    valid_target_file = os.path.commonpath([abs_working_directory, abs_file_path]) == abs_working_directory
    if not valid_target_file:
        return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory."
    if os.path.isdir(abs_file_path):
        return f"Error: Cannot write to \"{file_path}\" as it is a directory."
    try:
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)  # Ensure the directory exists
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return f"Successfully wrote to \"{file_path}\"({len(content)} characters written.)"
    except PermissionError:
        return f"Error: Permission denied to write to \"{file_path}\"."
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to write file to, relative to the working directory (default is the working directory itself)",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
    ),
)