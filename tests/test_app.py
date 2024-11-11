import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World from Yasmeen Lamaa!")

if __name__ == "__main__":
    unittest.main()
