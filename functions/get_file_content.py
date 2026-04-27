import os

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    full_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    if not os.path.commonpath([working_dir_abs, full_file_path]) == working_dir_abs:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        MAX_CHARS = 10000
        with open(full_file_path, 'r') as f:
            content = f.read(MAX_CHARS)

        if len(content) == MAX_CHARS:
            content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


 