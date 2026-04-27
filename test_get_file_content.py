from functions.get_file_content import get_file_content

def main():
    print("Test 1: lorem.txt")
    result1 = get_file_content("calculator", "lorem.txt")
    if "truncated" in result1:
        print("Pass")
    else:
        print("Fail")

    print("\nTest 2: main.py")
    result2 = get_file_content("calculator", "main.py")
    print(result2)

    print("\nTest 3: pkg/calculator.py")
    result3 = get_file_content("calculator", "pkg/calculator.py")
    print(result3)

    print("\nTest 4: /bin/cat (should error)")
    result4 = get_file_content("calculator", "/bin/cat")
    print(result4)

    print("\nTest 5: pkg/does_not_exist.py (should error)")
    result5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result5)

if __name__ == "__main__":
    main()


