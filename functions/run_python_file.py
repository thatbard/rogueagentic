import os
import subprocess
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Takes the file path and arguments for a Python file to be run as a subprocess",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to a Python file relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="List of arguments to be passed to subprocess at file_path"
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        val = ''
        
        # Will be True or False
        valid_file_path = os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not (file_path[-3:] == '.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", file_path_abs]
        
        result = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)

        if result.returncode:
            val += f'Process exited with code {result.returncode}'
        if result.stdout == False and result.stderr == False:
            val += 'No output produced'
        if result.stdout:
            val += f"STDOUT: {result.stdout}"
        if result.stdout:
            val += f"STDERR: {result.stderr}"

        return val

    except Exception as e:
        return f'Error: executing Pyton file: {e}'