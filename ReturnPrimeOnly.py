__author__ = 'student'


import math

numbers = input('give me a number ')
primes = [2, ]

#this is the set of numbers up to a user defined end, but we can step by 2 because all even numbers are not prime
for number in range(3, numbers + 1):
    differences = []
    prime = number > 0
#this is the set of numbers to divide into the user defined numbers
    for test in range(2, number):
        # the following formula takes the number (floated to a decimal) divided by the test(same) to create a quotient
        # if the quotient minus its floor (rounded down) is decimal it could be prime.
        print (number, test)
        #quotient = float(number) / float(test)
        #difference = quotient - math.floor(quotient)
        #differences.append(difference)
        #if all(differences) >0:
            #primes.append(number)
        #if 0 in differences:


        #print (number, test, differences)
        # if the result is 0 it is not a prime
        #if difference == 0:
            #break
        #elif difference != 0:

            #print (number, test, difference)
            #if all(differences) > 0:
                #print (number)
           # break

        #primes.append(number)
#for i in primes:
    #print(i)




