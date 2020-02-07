import unittest
from sum import custom_sum


class MyTestCase(unittest.TestCase):
    def test_custom_sum(self):
        self.assertEqual(custom_sum(1, 1), 2)


if __name__ == '__main__':
    unittest.main()
