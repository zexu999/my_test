import contextlib
import io
import subprocess
import sys
import unittest
from pathlib import Path

import hello

HELLO = Path(__file__).with_name("hello.py")


class HelloTest(unittest.TestCase):
    def test_main_prints_greeting(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            hello.main()
        self.assertEqual(out.getvalue(), "Hello, world!\n")

    def test_script_prints_greeting(self):
        result = subprocess.run(
            [sys.executable, str(HELLO)], capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, world!\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
