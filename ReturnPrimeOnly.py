__author__ = 'student'


import math

numbers = input('give me a number ')
#numbers2 = (numbers + 1)
primes = [2, ]

#this is the set of numbers up to a user defined end
for number in range(1, numbers + 1):
    #this is the set of numbers to divide into the user defined numbers
    for test in range(2, number):
        # this formula takes the number divided by the test to create a quotient
        # but, it makes the number and test variables floats so that we can return an number with decimals
        # if the quotient minus the floor or rounded down number is decimal it is a prime
        quotient = float(number) / float(test)
        difference = quotient - math.floor(quotient)

        # if the difference is a whole number then it is not a prime and the following send the program back up to the neginning
        if difference == 0:
            break
        # here the decimal is registered as a prime and the break stops it from repeating with repeated tests
        else:
            primes.append(number)
            break
        #to-do make the list fabulous!
        #print (str(number), str(quotient), str(difference)) - a test to see how the numbers are interacting in the loops

for i in primes:
    print(i)




