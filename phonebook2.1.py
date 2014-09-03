print('Welcome to your phone book')
Phone = {}
firstnamedict = {}
numberdict={}
while True:
   
# Menu

   
    print('*************************************')
    print('Press 1 to add an entry-')
    print('Press 2 to delete an entry-')
    print('Press 3 to find an entry-')
    print('Press 4 to edit an entry-')
    print('Press 5 to list entries-')
    print('Press Q to quit-')
    print('*************************************')
    
    firstchoice = raw_input('=>>').lower()
   
#####print firstchoice
#####print type(firstchoice)


#option 1 add an entry
    if firstchoice == '1':
        firstname = raw_input('What is your first name? ')
	lastname = raw_input('What is your last name? ')
        number = raw_input('What is your phone number? ')
        Saddress = raw_input('What is your street address? ')
    	Tempdictlastname = {lastname: [firstname, lastname, number, Saddress]}
        #create dictionary for firstname and last name
	Tempdictfirstname =  {firstname: [firstname, lastname, number, Saddress]}
	Tempdictnumber	=  {number: [firstname, lastname, number, Saddress]}
	
        #print Tempdict
	#print Phone
        Phone.update(Tempdictlastname)
	firstnamedict.update(Tempdictfirstname)
	numberdict.update(Tempdictnumber)
        #print Phone
	print('\n')
        print Phone[lastname] 
        print ('\n' * 2)
#to-do  present inputs nicely



#option 2 delete an entry
    elif firstchoice == '2':
    #print('xx')
        deleteAsk = raw_input('To delete an entry, please enter last name.')
	Phone.pop(deleteAsk)
	print Phone
    







#option 3 find an entry
    elif firstchoice == '3':
        #print('yy')
	print('Would you like to search by: ')
	print('	A: Last Name')
	print('	B: First Name')
	print('	C: Number') 
	searchby = raw_input('Enter a letter => ').lower()
	#print type(searchby)

	if searchby == 'a':
	    namequery = raw_input('	Enter last name: ')
	    #print type(namequery)	
	    if namequery in Phone:
	        print  "\t \t" + str(Phone[namequery])
	    	print('\n \n')
	    else:
	        print "BEEP!!!!!!"
		print "Try again!!" 
		True

	###try to create a new dictionary key based on choice?

        elif searchby == 'b':
	    namequery = raw_input('	Enter first name: ')
	   #print type(namequery)......is there a kew variable?	
	    if namequery in firstnamedict:
	        print  "\t \t" + str(firstnamedict[namequery])
	    	#print('\n \n')
	    else:
	        ##print "BEEP!!!!!!"
		##print "Try again!!"
                True 

        elif searchby == 'c':
            namequery = raw_input('    Enter phone number: ')
	    if namequery in numberdict:
	        print  "\t \t" + str(numberdict[namequery])
	    	#print('testing')
            else:
	        print "BEEP!!!!!!"
		##print "Try again!!" 
                True
		
        else:
	    print('Try again.....follow instructions. Please and thank you.')	

         





#option 4 edit an entry
    elif  firstchoice == '4':
        #print('zz')
	#Edit field by last name only

	editquery = raw_input("Enter last name ")
	if editquery in Phone:
	    print Phone[editquery]
	    edit_y_or_n = raw_input("Is this correct? ").lower()
	    if edit_y_or_n == 'n':

		#Edit choices
		print('Which field would you like to edit?')
		print('Press A for phone number')
		print('Press B for address')
		print('(If you want to change a name.....lets just start over)')
		
	        editfield = raw_input('==>').lower()

		if editfield == 'a':
		    new_number = raw_input('Please enter the new number: ')
#Test print path to number
		    Phone[editquery][2] = new_number
		    print Phone[editquery]

		elif editfield == 'b':
		    new_address = raw_input('Please enter the new address: ')
#print path to address	
		    Phone[editquery][3] = new_address
		    print Phone[editquery]
	
		else:
		    True
	    else:
	        True		
	else:
	    True
	


#option 5 list entries
    elif firstchoice == '5' :
	print Phone

#Option Q
    elif firstchoice == 'q':
        break

#Menu soon to be a repeat function
    else:
       True






