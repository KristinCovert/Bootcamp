__author__ = 'Kristin'


class Contact():
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address

print type(Contact)

print dir(Contact)

tim = Contact('Tim', 8675309, '123 SE Tolman')

print(tim.name)

friend = tim
person = friend

tim.address = '123 Elm St.'

print (person.number)

print (tim.name, tim.number, tim.address)