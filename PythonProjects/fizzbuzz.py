a = 0
b = 22

while a <= b:
    if a % 3 == 0 and a % 4 == 0:
        print ('fizzbuzz')
        if a == b:
            break
        else:
            a +=1
    if a % 3 == 0:
        print ('fizz')
        if a == b:
            break
        else:
            a +=1
    if a % 4 == 0:
        print ('buzz')
        if a == b:
            break
        else:
            a +=1
    else:
        print (a)
        a +=1


#        if a % 3 == 0 and a % 4 == 0:
 #           print ('fizzbuzz')
  #          a +=1
   #     else:
    #    print ('buzz')
     #   a +=1
#    if a == b:
#        print (a-1)
#        break
    #else:
    #    print (a)
    #    a +=1



