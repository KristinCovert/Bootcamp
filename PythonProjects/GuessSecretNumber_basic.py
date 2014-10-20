__author__ = 'Kristin & Kalyani'

import random

print ('Welcome to Choose a number')

secret = random.randint(1, 10)

guess = input('Enter a number to guess: ')

#counter = 0

#While counter < 5:
if guess == secret:
    print "Yeah! you got the number!"
if guess > secret:
    print "Too high"
        #counter += 1
if guess < secret:
    print "Too low"
        #counter += 1
else:
    print ('Nope, the number was:')
    print (secret)







