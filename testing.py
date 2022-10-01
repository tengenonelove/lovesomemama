import unittest
from max import mel

class Testmel(unittest.TestCase):
    def test_mel(self):
        self.assertEqual(mel(2), 6)

if __name__ == "__main__":
    unittest.main()
    
