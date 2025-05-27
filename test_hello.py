import unittest
import subprocess
import sys

class TestHelloWorld(unittest.TestCase):

    def test_hello_world_output(self):
        # Run the hello.py script as a subprocess
        process = subprocess.Popen(
            [sys.executable, 'hello.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()

        # Check if the script ran successfully
        self.assertEqual(process.returncode, 0, f"Script exited with error: {stderr}")

        # Check the output
        self.assertEqual(stdout.strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
