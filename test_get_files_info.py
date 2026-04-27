from functions.get_files_info import get_files_info

def main():

    result = [0, 0, 0, 0]

    if get_files_info("calculator", ".") == '''Result for current directory:
  - pkg: file_size=4096 bytes, is_dir=True
  - tests.py: file_size=1403 bytes, is_dir=False
  - main.py: file_size=830 bytes, is_dir=False''':
        result[0] = 1
        print("Test 1 pass")

    if get_files_info("calculator", "pkg") == '''Result for 'pkg' directory:
  - render.py: file_size=419 bytes, is_dir=False
  - __pycache__: file_size=4096 bytes, is_dir=True
  - calculator.py: file_size=1813 bytes, is_dir=False''':
        result[1] = 1
        print("Test 2 Pass")

    if get_files_info("calculator", "/bin") == '''Result for '/bin' directory:
    Error: Cannot list "/bin" as it is outside the permitted working directory''':
        result[2] = 1
        print("Test 3 Pass")

    if get_files_info("calculator", "../") == '''Result for '../' directory:
    Error: Cannot list "../" as it is outside the permitted working directory''':
        result[3] = 1
        print("Test 4 Pass")

    print(f"Test results: {result}")
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "pkg"))
    print(get_files_info("calculator", "/bin"))
if __name__ == "__main__":
    main()
