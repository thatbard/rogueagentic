import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        val = ''
        
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{target_dir}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{target_dir}" is not a directory'
        
        for item in os.listdir(target_dir):
            cur_item = target_dir + '/' + item
            val = val + f'- {os.path.basename(cur_item)}: file_size={os.path.getsize(cur_item)}, is_dir={os.path.isdir(cur_item)}' + '\n'

        return val

    except Exception as e:
        return f'Error: {e}'