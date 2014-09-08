__author__ = 'student'


import random


def make_secret(difficulty):
    return random.randint(1, difficulty)


def choose_difficulty():

    print ("""Welcome to Choose a number!
Let's begin.""")

    user_prompt = raw_input("""

Choose a difficulty:

easy: 4 guesses for a number in 1 - 10
moderate: 10 guesses for a number in 1 - 50
difficult: 20 guesses for a number in 1 - 100: """)

    difficulty_options = {'easy': (4, 10), 'moderate': (10, 50), 'difficult': (20, 100)}

    number_of_guesses = difficulty_options[user_prompt][0]

    secret = make_secret(difficulty_options[user_prompt][1])

    return number_of_guesses, secret


def play_again():
    response = raw_input("Do you want to play again? Y or N: ").upper()
    if response == 'Y':
        play()
    else:
        print 'Thanks for playing!'
        exit()


def user_guess():
    guess = input("Please enter a number: ")
    return guess


def play():

    (guess_range, secret) = choose_difficulty()
    print "{} is the secret and {} is the range".format(secret, guess_range)
    counter = 0

    while counter < guess_range:
        guess = user_guess()
        if guess > secret:
            print "Too high"
            counter += 1
            print counter
        if guess < secret:
            print "Too low"
            counter += 1
            print counter
        if guess == secret:
            print "You got it!"
            break
    else:
        print("you are out of guesses")

#choose_difficulty()
play()
play_again()