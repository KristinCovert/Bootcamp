__author__ = 'Kristin & Kalyani - k&k games'

#import the random number generator
import random


#make the secret number using random library and 'randomint' option.
# on the range of 1 to a number representing the difficulty of the game & chosen by the user.
def make_secret(difficulty):
    return random.randint(1, difficulty)

#choose the difficulty of the game which sets the number of guesses the player has
#and the top of the range from which the secret number os generated
def choose_difficulty():

    print ("""
Welcome to Choose a number!
Let's begin.""")

    user_prompt = raw_input("""
Choose a difficulty by typing one of the levels below:
    easy: 4 guesses for a number in 1 - 10
    moderate: 8 guesses for a number in 1 - 50
    difficult: 12 guesses for a number in 1 - 200
    : """)

    difficulty_options = {'easy': (4, 10), 'moderate': (8, 50), 'difficult': (12, 200)}

    number_of_guesses = difficulty_options[user_prompt][0]

    secret = make_secret(difficulty_options[user_prompt][1])

    return number_of_guesses, secret


#allows the user to play again
def play_again():
    response = raw_input("""
    Do you want to play again?
    Y or N: """).upper()
    if response == 'Y':
        play()
    else:
        print 'Thanks for playing!'
        exit()


#takes the user's first-n guess and runs it through the game
def user_guess():
    guess = input("Please enter a number: ")
    return guess


#when choosing the most difficult level, the tests for determining if the guess
#is higher or lower than the secret changes to two levels. This helps the user
# determine if they are really close, close, far or really far away.
def clues_difficult(guess, secret):
    #print secret
    if secret + 20 > guess > secret:
        print "Close but, too high"
    if secret - 20 < guess < secret:
        print "Too low"
    if guess >= secret + 20:
        print "Hold on there Nelly, way to high"
    if guess <= secret - 20:
        print "Oh my, that's way too low"


#the play function pulls the number of guesses and secret from the choose difficulty
#function and runs it through either set of tests to determine how close each guess is
#to the secret based on a counter that is set by the number of guesses.  Play again is
#within this function so that it repeats for as long as the user wants.
def play():

    (guess_range, secret) = choose_difficulty()

    counter = 0

    while counter < guess_range:
        guess = user_guess()
        if guess_range <= 8:
            if guess > secret:
                print "Too high"
            if guess < secret:
                print "Too low"
            counter += 1
        if guess_range == 12:
            clues_difficult(guess, secret)
            counter += 1
        if guess == secret:
            print "You got it, Einstein!"
            break
    else:
        print("You are out of guesses, the secret was {}!".format(secret))
    play_again()
#The actual running of the game in just one pretty little lines
play()
