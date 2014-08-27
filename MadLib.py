#The following is the Mad Lib story with place holders for user inputs.
story  = """
There once was a programmer named %(name)s.
%(name)s loves to %(verb)s.
%(name)s especially likes to %(verb)s when programming!
But it is important when %(verb2)s to also wear your %(noun)s.
%(adj)s %(name)s!
Perhaps %(name)s should %(verb3)s her %(noun)s while programming! 
"""
#Here we define what the user will input to fill in the place holders.
name = raw_input("Please give us a name")
verb = raw_input("Please give us a verb")
noun = raw_input("Please give us a noun")
adj = raw_input("Please give us an adjective")
verb3 = raw_input("Please give us another verb")
#Here the placeholders from the story are matched to the user defined place holders.
variables = {'name': name, 'verb': verb, 'verb2' : verb + 'ing', 'noun' : noun, 'adj' : adj.capitalize(), 'verb3' : verb3}
#This is the finished story.
print (story % variables)
