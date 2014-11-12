#user input
name = raw_input('what is your name?')
color = raw_input('What is your favorite color?')
food = raw_input('What is your favorite food?')
tree = raw_input('What is your favorite tree?')

#insert variables in dictionary
madlist = {'n': name, 'c': color, 'f': food,'t': tree}

#story
story = 'Hello %(n)s, why are you wearing a %(c)s hat made out of %(f)s?\nHats are usually made out of %(t)s.'

#result
print story % madlist

