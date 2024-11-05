import unittest

def basic_addition(x, y):
    return x + y

class TestAddFunction(unittest.TestCase):
    def test_basic_addition(self):
        self.assertEqual(basic_addition(2, 3), 5)
        self.assertEqual(basic_addition(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()