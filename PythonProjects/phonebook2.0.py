
Phone = {}

while True:

# Menu

    print('Welcome to your phone book')
    print('*************************************')
    print('Press 1 to add an entry-')
    print('Press 2 to delete an entry-')
    print('Press 3 to find an entry-')
    print('Press 4 to edit an entry-')
    print('Press 5 to list entries-')
    print('Press Q to quit-')
    print('*************************************')
    
    firstchoice = raw_input('=>>')

#####print firstchoice
#####print type(firstchoice)


#option 1 add an entry
    if firstchoice == '1':
        firstname = raw_input('What is your name? ')
	lastname = raw_input('What is your last name? ')
        number = raw_input('What is your phone number? ')
        Saddress = raw_input('What is your street address? ')
    	Tempdict = {lastname: [firstname, lastname, number, Saddress]}
        print Tempdict
	#print Phone
        Phone.update(Tempdict)
        print Phone






#option 2 delete an entry
    elif firstchoice == '2':
    #print('xx')
        deleteAsk = raw_input('To delete an entry, please enter last name.')
	Phone.pop(deleteAsk)
	print Phone
    







#option 3 find an entry
    elif firstchoice == '3':
        #print('yy')
	print('Would you like to search by:')
	print('	A: Last Name')
	print('	B: First Name')
	print('	C: Number') 
	searchby = raw_input('Enter a letter =>').lower()
	print type(searchby)
#
	if searchby == 'a':
	    namequery = raw_input('	Enter last name: ')
	    	
  	elif searchby == 'b': 
	    namequery = raw_input('	Enter Fast name: ')
	    		
	elif searchby == 'c':
	    namequery = raw_input('	Enter number: ')
	    	
	else :
	    print('Try again.....follow instructions. Please and thank you.')	

         





#option 4 edit an entry
    elif  firstchoice == '4':
        print('zz')



#option 5 list entries
    elif firstchoice == '5' :
	print Phone

#Option Q
    elif firstchoice == 'q' or 'Q':
        break

#Menu soon to be a repeat function
    else:
       True

 #




