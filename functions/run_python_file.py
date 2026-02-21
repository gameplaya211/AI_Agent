import os
from google.genai import types
def run_python_file(working_directory, file_path, args=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(abs_working_directory, file_path))
    valid_target_file = os.path.commonpath([abs_working_directory, abs_file_path]) == abs_working_directory
    if not valid_target_file:
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory."
    if not os.path.isfile(abs_file_path):
        return f"Error: \"{file_path}\" does not exist or is not a regular file."
    if not abs_file_path.endswith('.py'):
        return f"Error: \"{file_path}\" is not a Python file."
    try:
        import subprocess
        command = ['python', abs_file_path]
        if args:
            command.extend(args)
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if result.stdout.strip() == '' and result.stderr.strip() == '':
            return "No output produced"
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file in the specified working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to run Python file in, relative to the working directory (default is the working directory itself)",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Arguments to pass to the Python file",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)