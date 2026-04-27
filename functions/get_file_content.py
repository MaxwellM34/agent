def get_file_content(working_directory, file_path):
    try:
        if not os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs:
            print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(file_path):
            print(f'Error: File not found or is not a regular file: "{file_path}"')
    
    MAX_CHARS = 10000
    with open(file_path, 'r') as f:
        content = f.read(MAX_CHARS)
        if len(content) == MAX_CHARS:
            print(f'Warning: File content truncated to {MAX_CHARS} characters.')
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content

        

    catch Exception as e:
        print(f'Error: {e}')
