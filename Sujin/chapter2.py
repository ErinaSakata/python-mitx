""" write a program that examines three variables-x,y, and z- and prints the largest odd number among them. /
/*-- If none of them are ood, it should print a message to that effect """


x = 7
y = 8
z = 1

""" answer should be y = 5 """


if (x % 2 == 1 and y % 2 == 1 and z % 2 == 1):
    if x < y < z : 
        print "z is the largest number"
    elif z < x < y:
        print "y is the largest number"
    else: 
        print "x is the largest number"
elif (x % 2 == 1 or y % 2 == 1 or z % 2 == 0):
    if x < y < z : 
        print "z is the largest number"
    elif z < x < y:
        print "y is the largest number"
    else: 
        print "x is the largest number"



else:
    print "there is no odd number"
    
print 'end of code'    