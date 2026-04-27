import os

def get_files_info(working_directory, directory="~/workspace/bootdev/agent"):
    working_dir_abs = os.path.abspath(directory)
    print(working_dir_abs)
    print(f"hello{os.path.abspath(directory)}")
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    os.path.commonpath()


def main():
    get_files_info("agent")

if __name__ == "__main__":
    main()
