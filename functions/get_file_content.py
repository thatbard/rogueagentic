import os
# from ..config import MAX_FILE_READ


MAX_FILE_READ = 10000


def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        content = ''
        
        # Will be True or False
        valid_file_path = os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(file_path_abs, "r") as f:
            content = f.read(MAX_FILE_READ)

            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_FILE_READ} characters]'

        return content

    except Exception as e:
        return f'Error: {e}'