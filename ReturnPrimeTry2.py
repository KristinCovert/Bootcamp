__author__ = 'student'


import math

#user defined number to check for primes up to
numbers = input('give me a number ')
#The ultimate list of primes that will print once the program is done running
primes = []

#This is the outer loop
for number in range(2, numbers + 1):
    #** here the prime is false statement is checked with the statement below.  If the answer to the difference was 0
    #prime was false and does not match the prime is true statement and we stop.  If the answer is a decimal then we go
    #to the outer loop end below ***
    prime = True
    #print (number)
    #This is my inner loop
    for test in range(2, number):
        #print (test)
        #The following tests if a number is 0 or a decimal after it is divided by itself + 1 up to itself -1.
        quotient = float(number) / float(test)
        #print (quotient)
        difference = quotient - math.floor(quotient)
        #print (difference)
        #Here we determine if the difference is 0 or a decimal and if it is 0 then it is not a prime.
        if difference == 0:
            #when we get a 0 prime is false so we go tot he outer loop see ** above
            prime = False
    #***which is true thus moving onto the command below, which puts the number in the primes list,
    if prime is True:
        primes.append(number)
print(primes)