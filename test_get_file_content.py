from functions.get_file_content import get_file_content
import os
def test_get_file_content():
    print("Result for 'main.py':")
    print(get_file_content("calculator", "main.py"))
    print("\nResult for 'pkg/calculator.py':")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\nResult for '/bin/cat':")
    print(get_file_content("calculator", "/bin/cat"))
    
    print("\nResult for 'pkg/does_not_exist.py':")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
test_get_file_content()