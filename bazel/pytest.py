import json
import os
import sys

import pytest

print("TROLOLO " + os.environ.get("PYTHONPATH"))
print("TROLOLO " + os.getcwd())
print("TROLOLO " + str(sys.path))

sys.exit(pytest.main(["--color=yes", "-s"]))
