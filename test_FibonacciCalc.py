__author__ = 'student'

import unittest
import HibinachiCalc


class MyTestCase(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(HibinachiCalc.fibonacci(), [1, 2, 3, 5, 8])


if __name__ == '__main__':
    unittest.main()
