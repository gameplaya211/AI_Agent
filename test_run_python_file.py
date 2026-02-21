import os
from functions.run_python_file import run_python_file
def test_run_python_file():
    print("Result for running calculator.py with no arguments:")
    print(run_python_file("calculator", "main.py"))
    print("\nResult for running calculator.py with arguments:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("\nResult for running calculator tests.py:")
    print(run_python_file("calculator", "tests.py"))
    print("\nResult for inputting an invalid path:")
    print(run_python_file("calculator", "../main.py"))
    print("\nResult for inputting a nonexistant file:")
    print(run_python_file("calculator", "nonexistent.py"))
    print("\nResult for inputting a non-python file:")
    print(run_python_file("calculator", "lorem.txt"))
test_run_python_file()