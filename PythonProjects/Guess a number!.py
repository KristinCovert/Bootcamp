__author__ = 'Kristin & Kalyani'

import random

print ('Welcome to Choose a number')

secret = random.randint(1, 10)
print secret
#guesses = 5
counter = 0
#n = input('Enter a number to guess: ')
guessno=raw_input("Enter a number to guess: ")

def guess():
    return guessno

guess()

while counter <= 5:

    if guessno == secret:
        print "Yeah! you got the number!"

    if guessno > secret:
        print "Too high"
        counter +=1
        guess()

    if guessno < secret:
        print "Too low"
        counter += 1
        guess()

print ('Nope, the number was:')
print (secret)

#counter += 1






