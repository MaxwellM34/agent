import os

def write_file(working_directory, file_path, content):

    working_dir_abs = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    if not os.path.commonpath([working_dir_abs, file_path]) == working_dir_abs:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    try:
        os.mkdirs(file_path, exist_ok=True)
        with open(file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: {e}'
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
