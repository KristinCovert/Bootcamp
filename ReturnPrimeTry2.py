__author__ = 'student'


import math

numbers = input('give me a number ')
primes = []

for number in range(2, numbers + 1):
    prime = True
    #print (number)
    for test in range(2, number):
        #print (test)
        quotient = float(number) / float(test)
        #print (quotient)
        difference = quotient - math.floor(quotient)
        #print (difference)
        #maybe 0.0
        if difference == 0:
            prime = False
    if prime is True:
        primes.append(number)
print(primes)