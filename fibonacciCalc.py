__author__ = 'Kristin'

def range_top():
    range_top = input('Up to what number would you like to calculate the Fibonacci')
    return range_top()

def fibonacci():
    i = 0
    j = 1
    fibonacci_list = []
    for number in range(0, range_top()):
        k = i + j
        fibonacci_list.append(k)
        i = j
        j = k
    return fibonacci_list

fibonacci()
print fibonacci()
