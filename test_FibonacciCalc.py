__author__ = 'student'

import unittest
import fibonacciCalc


class test_fibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacciCalc.fibonacci(5), [1, 2, 3, 5, 8])

    def test_fibonacci_length(self):
        rt = 10
        result = fibonacciCalc.fibonacci(rt)
        l = len(result)
        self.assertEqual(rt, l)


if __name__ == '__main__':
    unittest.main()
