__author__ = 'Kristin'

#The following is the original Mad Lib story with place holders for user inputs.
# story  = """
# There once was a programmer named %(name)s.
# %(name)s loves to %(verb)s.
# %(name)s especially likes to %(verb)s when programming!
# But it is important when %(verb2)s to also wear your %(noun)s.
# %(adj)s %(name)s!
# Perhaps %(name)s should %(verb3)s her %(noun)s while programming!
# """
# #Here we define what the user will input to fill in the place holders.
# name = raw_input("Please give us a name")
# verb = raw_input("Please give us a verb")
# noun = raw_input("Please give us a noun")
# adj = raw_input("Please give us an adjective")
# verb3 = raw_input("Please give us another verb")
# #Here the placeholders from the story are matched to the user defined place holders.
# variables = {'name': name, 'verb': verb, 'verb2': verb + 'ing', 'noun': noun, 'adj' : adj.capitalize(), 'verb3' : verb3}
# #This is the finished story.
# print (story % variables)
#


class Story():
    def __init__(self):
        self.name = raw_input("Please give us a name ")
        self.verb = raw_input("Please give us a verb ")
        self.verb2 = self.verb + 'ing'
        self.noun = raw_input("Please give us a noun ")
        self.adj = raw_input("Please give us an adjective ")
        self.verb3 = raw_input("Please give us another verb ")
        self.story = """
            There once was a programmer named %(name)s.
            %(name)s loves to %(verb)s.
            %(name)s especially likes to %(verb)s when programming!
            But it is important when %(verb2)s to also wear your %(noun)s.
            %(adj)s %(name)s!
            Perhaps %(name)s should %(verb3)s her %(noun)s while programming!
            """
        self.story2 = """
            There once was a programmer named {name}.
            {name} loves to {verb}.
            {name} especially likes to {verb} when programming!
            But it is important when {verb2} to also wear your {noun}.
            {adj} {name}!
            Perhaps {name} should {verb3} her {noun} while programming!
            """

    # story = """
    # There once was a programmer named %(self.name)s.
    # %(self.name)s loves to %(self.verb)s.
    # %(self.name)s especially likes to %(self.verb)s when programming!
    # But it is important when %(self.verb2)s to also wear your %(self.noun)s.
    # %(self.adj)s %(self.name)s!
    # Perhaps %(self.name)s should %(self.verb3)s her %(self.noun)s while programming!
    # """

    def return_story(self):
        variables = {'name': self.name, 'verb': self.verb, 'verb2': self.verb + 'ing', 'noun': self.noun, 'adj' : self.adj.capitalize(), 'verb3' : self.verb3}
        print(self.story % variables)
        print (self.story % (self.name,
                             self.name,
                             self.verb,
                             self.name, self.verb,
                             self.verb2, self.noun,
                             self.adj.capitalize(), self.name,
                             self.name,
                             self.verb3, self.noun))

    def return_story2(self):
        self.story2.format(name=self.name, verb=self.verb, noun=self.noun, adj=self.adj, verb2=self.verb2, verb3=self.verb3)
        return self.story2




grants_story = Story()

print(grants_story.return_story2)

# def compare(story1, story2):
#     """
#     :param story1:
#     :param story2:
#     :return: resturns similarityof two stories

#moniques_story = Story()

#moniques_story.return_story()
