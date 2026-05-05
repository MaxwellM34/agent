from functions.write_file import write_file
from functions.get_file_content import get_file_content

def main():
    write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

    result = [0, 0, 0]

    if "wait, this isn't lorem ipsum" in get_file_content("calculator", "lorem.txt"):
        result[0] = 1
    if "lorem ipsum dolor sit amet" in get_file_content("calculator/pkg", "morelorem.txt"):
        result[1] = 1
    if not "this should not be allowed" in get_file_content("calculator/tmp", "temp.txt"):
        result[2] = 1

    print(result)
    return

if __name__ == "__main__":
    main()
   