# user input
firstname = raw_input('What is your first name?')
lastname = raw_input('What is your last name?')
number = raw_input('What is your phone number?')
Saddress = raw_input('What is your street address?')

#Defining key
name =(lastname)
print type(name)
#Defining value
fulladdress = (firstname,lastname, number, Saddress)


#Create dicionary
Phone = {name: fulladdress}

#Search dictionary
query = raw_input('To check your entry, please enter last name.')

print Phone[query] 

#print phone(name)

firstname = raw_input('What is your first name?')
lastname = raw_input('What is your last name?')
number = raw_input('What is your phone number?')
Saddress = raw_input('What is your street address?')
#Defining key
name =(lastname)

#Defining value
fulladdress = (firstname,lastname, number, Saddress)

Phone[name] = fulladdress

#0print Phone

#Search dictionary
query = raw_input('To find someone, please enter last name.')

print Phone[query]

#delete entry

deleteAsk = raw_input('To delete an entry, please enter last name.')

Phone.pop(deleteAsk)

print Phone


