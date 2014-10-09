__author__ = 'Kristin'

import random
import re
import nltk

#slang and add-in dictionaries
slang_dict = {'really': ['hella', 'totally', 'fully'], 'gross': ['grody', 'gag me']}
add_ins = [', so, ', ', like, ', ' OMG ']

#split story into list, list words can be searched and replaced
story = ("You are really cool. Sand in my sandwich, gross! You're sweet. I am fun. "
         "That's cool!")

#TODO have the split of the text use spaces to do so but it needs to recognize when the word is a contraction and leave punctuation in.

def deconstruct_text():
    text_split = re.split(("[\w']+"), story)
    print text_split
    return text_split

#Here I get 5 random locations to swap random words in


def random_location():
    locations = []
    count = 0
    while count < 5:
        location = random.randint(1, len(story))
        locations.append(location)
        count += 1
    print locations
    return locations

There once was a really nice programmer.  He had a gross sandwich.  But class was realy fun!
#Here I use the random locations in the locations list to replace the location with a
#random selection from the add in list. I want this to iterate through the list of
#locations. So this is swapping not inserting.
def random_add():
    text_split = deconstruct_text()
    locations = random_location()
    for location in locations:
        add = random.choice(add_ins)
        text_split.insert(location, add)
    return text_split


text_split_final = random_add()
CAspeak = ' '.join(text_split_final)
print CAspeak

#TODO figure out the replace to take care of the problems in punctuation
# def pattern_resolve():
#     CAspeak.replace(', ,', ', ')
#     CAspeak.replace(', !', '!')
#     CAspeak.replace(' ,', ',')
#     return CAspeak


# pattern_resolve()
# print CAspeak

#patterns to replace: " ," with ","       '


#     for place in text_split:
#         if place == '. ':
#             text_split.insert(random_location, '. Dude')
#         if place[0].isupper():
#             text_split.insert(text_split.index(place), 'So')
#     return text_split
#
# def replace_word_slang(self, text_split):
#         for word in text_split:
#             for slang in slang_dict:
#                 if word == slang:
#                     print (word, random.choice(slang_dict[slang]))
#                     slang_choice = random.choice(slang_dict[slang])
#                     text_split[text_split.index(word)] = slang_choice
#                     return text_split



# def add_in_dude():
#     for word in text_split:
#         if word == '!':
#             text_split.insert(text_split.index(word), '! Dude.')
#             return text_split

#random_add()
#''.join(text_split)
#print text_split

    #take a random location and put in Dude after a sentence and So before a sentence


#     def random_dude(self):
#         for place in text_split:
#             if place == '. ':
#                 random_location = random.randint(1, len(text_split))
#                 print random_location
#                 text_split.insert(random_location, '. Dude')
#             if place[0].isupper():
#                 text_split.insert(text_split.index(place), 'So,')
#
# Kristin = CAspeak_translate()
# print Kristin
# # replace_word_slang()
# # add_in_dude()
# # random_dude()
# # print(text_split)
