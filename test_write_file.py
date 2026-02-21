from functions.write_file import write_file
import os
def test_write_file():
    print("Result for editing lorem.txt:")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("\nResult for 'adding morelorem.txt':")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("\nResult for 'changing tmp.txt':")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
test_write_file()