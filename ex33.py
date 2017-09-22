# This is how the extra credit looks before extra credit #5
#numbers = []
#
#def while_loop(i, j, increment):
#    while i < j:
#        print "At the top i is %d" % i
#        numbers.append(i)
#        
#        i = i + increment
#        print "Numbers now: ", numbers
#        print "At the bottom i is %d" % i
#        
#while_loop(0, 7, 2)
#    
#print "The numbers: "
#
#for num in numbers:
#    print num

# The following is the result of doing EC(Extra Credit) #5
numbers = []

for i in range(0,6): #add a third number into the range arguments to make increment other than 1, ie do (0,6,2) to go by 2's
    print "i is now %d" % i
    numbers.append(i)

    print "Numbers now: ", numbers


print "The numbers: "

for num in numbers:
    print num
