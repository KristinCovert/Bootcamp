__author__ = 'Kristin'


def range_top():
    top_range = input('Up to what number would you like to calculate the Fibonacci: ')
    return top_range


def fibonacci(rt):
    i = 0
    j = 1

    fibonacci_list = []

    for number in range(0, rt):
        k = i + j
        fibonacci_list.append(k)
        i = j
        j = k
    return fibonacci_list

if __name__ == '__main__':
    x = range_top()
    result = fibonacci(x)
    print result
    l = len(result)
    print l

