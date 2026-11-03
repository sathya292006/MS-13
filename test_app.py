
import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet(),
            "Hello from Modified CI/CD version2!"
        )

if __name__ == "__main__":
    unittest.main()
