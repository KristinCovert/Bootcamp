__author__ = 'Kristin'

class CalcSquare():
    def __init__(self):
        self.x = input('Please give us a number: ')

    def square(self):
        square = (self.x * self.x)
        print square

answer = CalcSquare()
answer.square()

