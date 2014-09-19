__author__ = 'Kristin'

import random
import time
from nltk.tokenize import RegexpTokenizer


#TODO make a place to name each story by a person's name - or way to give the stories names
def ca_speak_method():
    print """\nOh my god, you are like, totally awesome 'cause you want to be more californian.\n"""
    time.sleep(3)
    print """So Dude, to fully talk like a true Californian you must, like, embrace your inner slang mojo.\n"""
    time.sleep(4)
    choice = input("""\nSo how you gonna pour your soul out?
    \n\tYou can totally
    1: write your own story or
    2: follow some prompts to make a story?
    1 or 2 dude? """)
    return choice


def make_story():

    x = ca_speak_method()

    if x == 1:
        text = raw_input("""\nCool Dude! Then tell us your story!
    We need, like, 5 - 10 sentences.
    And go ahead, use that CA slang you already know!
    We might add a function to assess your california-ness!\n""")
        return text

    if x == 2:
        question1 = raw_input('''\nYou are at the beach.
    What does it look like? \nThe beach is ''')
        question2 = raw_input('''\nThere are some hotty surfers riding waves.
    Describe them to us. I see ''')
        question3 = raw_input('''\nYou are now taking a walk on the beach.
    Describe your walk and what you see. As I ''')
        question4 = raw_input('''\nThere is dead jelly fish on the sand as you walk.
    Describe the carcass or how you feel. I stumble on ''')
        question5 = raw_input('''\nWrap up your day and tell us what you do.''')

        text = str("The beach is " + question1 + 'I see' + question2 + "As I " + question3 + 'I stumble on' + question4 + question5)
        return text


story = make_story()


class CASpeakTranslate(story):
    def __init__(self):
        self.story = story
        self.slang_dict = {'really': ['hella', 'totally', 'fully'], 'gross': ['grody', 'gag me']}
        self.add_ins = [', so, ', ', like, ', ', OMG, ']
        self.score = 0
        self.locations = []

    def deconstruct_text(self, story):
        text_split = RegexpTokenizer("[\w']+|[.,!?;:-]")
        print(text_split.tokenize(story))
        return text_split

    def replace_word_slang(self, text_split):
        for word in text_split:
            for slang in self.slang_dict:
                if word == slang:
                    print (word, random.choice(self.slang_dict[slang]))
                    slang_choice = random.choice(self.slang_dict[slang])
                    text_split[text_split.index(word)] = slang_choice
                    return text_split

    def random_location(self, text_split, locations):
        count = 0
        while count < 10:
            location = random.randint(1, len(text_split))
            locations.append(location)
            count += 1
        return locations
#Here I use the random locations from the locations list to replace the location with a
#random selection from the add in list. I want this to iterate through the list of
#locations. So this is swapping not inserting.
    def random_add(self, text_split):
        for location in self.locations:
            add = random.choice(self.add_ins)
            text_split.insert(location, add)
        return text_split

    def add_in_dude(self, text_split):
        for element in text_split:
            if element == '!':
                text_split.insert(text_split.index(element), ', Dude!')
                text_split.remove('!')
        return text_split


 CAspeakTranslate = ' '.join(text_split)
 print CAspeakTranslate
#
#
#
# #take a random location and put in Dude after a sentence and So before a sentence
#
#
# def random_add():
#         if place[0].isupper():
#             text_split.insert(text_split.index(place), 'So')
#
# #within class call all methods
# #deconstruct_text(self.story)
# #replace_word_slang(self.story)
# #print replace_word_slang(self.story)
# #random_add()
# # print(text_split)
#
# #text_split join - at very end take nothing and join it together ''.join(text_split)
#
# # def make_CAspeak():
# #     prompts to get text
# #     return CAspeak(story)
# # #file_open = open(pronouns.txt)
#
# #slang_dict.keys creates list of keys
# def CA_score():
#     score = 0
#     if word in slang_dict.keys():
#         score +=1
#     return score
#
# #insdethe class have an attribute that is the score - that a method writes too
# # #replacing words with slang but randomly replacing when there are multiple
# # #slang words that mean the same thing
# #
# #compare files - are you getting any better?
# #def compare(story1, story2):
# #     """
# #     :param story1:
# #     :param story2:
# #     :return: returns similarity of two stories
# #
# # def play_again():
# #     response = raw_input( """
# #     Do you want to play again?
# #     Y or N: """).upper()
# #     if response == 'Y':
# #         play()
# #     else:
# #         print '\nSee you later Dude!'
# #         exit()