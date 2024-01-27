import json
import os
import sys

import pytest

import os

def delete_empty_init_files(directory):
    for root, dirs, files in os.walk(directory):
        if '__init__.py' in files:
            init_file_path = os.path.join(root, '__init__.py')
            # Check if the file is empty
            if os.path.getsize(init_file_path) == 0:
                print(f"Deleting empty __init__.py file: {init_file_path}")
                if init_file_path in [
                    # "./lib/project1/__init__.py",
                    # "./lib/__init__.py",
                    "./lib/project1/project1/__init__.py",
                ]:
                    print("Skipping project1/__init__.py")
                    continue
                os.remove(init_file_path)

delete_empty_init_files('.')

# print("TROLOLO " + os.environ.get("PYTHONPATH"))
# print("TROLOLO " + os.getcwd())
# print("TROLOLO " + str(sys.path))

# import project1.test_foo

# assert project1.test_foo.Foo.__module__ == "project1.test_foo"

# sys.exit(pytest.main(["--color=yes", "-s", "lib/project1/project1/test_foo.py"]))

sys.exit(pytest.main(["--color=yes", "-s", "--rootdir=."]))
