__author__ = 'student'

import unittest
import fibonacciCalc


class test_fibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacciCalc.fibonacci(5), [1, 2, 3, 5, 8])

    def test_fibonacci_length(self):
        x = 10
        result = fibonacciCalc.fibonacci(x)
        l = len(result)
        self.assertEqual(x, l)


if __name__ == '__main__':
    unittest.main()
