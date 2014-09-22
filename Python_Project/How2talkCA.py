__author__ = 'Kristin'

import random
import time
import re
from nltk.tokenize import RegexpTokenizer


#Welcome to translator & choice of how to put in text to translate
def ca_speak_method():
    print """\nOh my god, you are like, totally awesome 'cause you want to be more californian.\n"""
    #time.sleep(2.5)
    print """So Dude, to fully talk like a true Californian you must, like, embrace your inner slang mojo.\n"""
    #time.sleep(5)
    choice = input("""\nSo how you gonna pour your mojo out?
    We'll help by translating your words into california-ness! Oh yeah, bro!
    \n\tYou can totally
    1: write your own story or
    2: follow some prompts to make a story?
    1 or 2 dude? """)
    return make_story(choice)


#text input, two methods


def make_story(choice):

    if choice == 1:
        text = raw_input("""\nCool Dude! Then tell us your story!
    We need, like, 5 - 10 sentences.
    And go ahead, use that CA slang you already know!
    We might add a function to assess your california-ness!\n""")
        return text

    if choice == 2:
        question1 = raw_input('''\nYou are at the beach.
    What does it look like? \nThe beach is ''')
        question2 = raw_input('''\nThere are some hotty surfers riding waves.
    Describe them to us. I see ''')
        question3 = raw_input('''\nYou are now taking a walk on the beach.
    Describe your walk and what you see. As I ''')
        question4 = raw_input('''\nThere is dead jelly fish on the sand as you walk.
    Describe the carcass or how you feel. I stumble on ''')
        question5 = raw_input('''\nWrap up your day and tell us what you do.''')

        text = str("The beach is " + question1 + 'I see' + question2 +
                   "As I " + question3 + 'I stumble on' + question4 + question5)
        return text


#class cookie cutter to turn the story into a translated text


class CASpeakTranslate():
    def __init__(self, story):
        self.story = story
    locations = []
    text_split = []
    joined_text = None
    translated_story = None

#take story and split it into a list but don't undo contractions using NLTK
    def deconstruct_text(self):
        self.text_split = RegexpTokenizer("[\w']+|[.,!?;:-]")
        self.text_split = (self.text_split.tokenize(self.story))
        return self.text_split

#replace words with slang from dictionary (expand to reading big excel file)
    def replace_word_slang(self):
        slang_dict = {'really': ['hella', 'totally', 'fully'], 'gross': ['grody', 'gag me']}
        for word in self.text_split:
            for slang in slang_dict:
                if word == slang:
                    #print (word, random.choice(slang_dict[slang]))
                    slang_choice = random.choice(slang_dict[slang])
                    self.text_split[self.text_split.index(word)] = slang_choice
                    return self.text_split

#create random locations to replace with add-in words
    def random_location(self):
        count = 0
        while count < 5:
            location = random.randint(1, len(self.text_split))
            self.locations.append(location)
            count += 1
        return self.locations

#use locations made above to insert add-ins
    def random_add(self):
        add_ins = ['so,', 'like,', 'OMG,']
        for location in self.locations:
            add = random.choice(add_ins)
            self.text_split.insert(location, add)
        return self.text_split

#add in Dude after each !
    def add_in_dude(self):
        for element in self.text_split:
            if element == '!':
                self.text_split.insert(self.text_split.index(element), ', Dude!')
                self.text_split.remove('!')
        return self.text_split

#join the text
    def join_text(self):
        self.joined_text = ' '.join(self.text_split)
        return self.joined_text

#fix the punctuation
    def fix_punct(self):
        fix_1 = re.sub(r"(\s+\.)", ".", self.joined_text)
        fix_2 = re.sub(r"(\s+!)", "!", fix_1)
        fix_3 = re.sub(r"(\s+,)", ",", fix_2)
        fix_4 = re.sub(r"(\s+\?)", "?", fix_3)
        self.translated_story = re.sub(r"(\s+:)", ";", fix_4)
        return self.translated_story

story = ca_speak_method()
ca_speak = CASpeakTranslate(story)
ca_speak.deconstruct_text()
ca_speak.replace_word_slang()
ca_speak.random_location()
ca_speak.random_add()
ca_speak.add_in_dude()
ca_speak.join_text()
ca_speak.fix_punct()
print ca_speak.translated_story

#print ca_speak

#TODO compare stories 1 vs 2 after play again to see change in CAness

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