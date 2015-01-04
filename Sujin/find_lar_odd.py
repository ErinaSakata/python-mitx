""" write a program that examines three variables-x,y, and z- and prints the largest odd number among them. If one of them are odd, it should print a message to that effect """

x = int(raw_input("enter x : "))
y = int(raw_input("enter y : "))
z = int(raw_input("enter z : "))

""" answer should be y = 5 """

print "Start"

x_is_odd = True if x % 2 == 1 else False
y_is_odd = True if y % 2 == 1 else False
z_is_odd = True if z % 2 == 1 else False

if x_is_odd and y_is_odd and z_is_odd:
    if x < y < z : 
        print "z is the largest odd number. #1"
    elif z < x < y:
        print "y is the largest odd number. #2"
    else: 
        print "x is the largest odd number. #3"

elif x_is_odd :
    if y_is_odd and not z_is_odd:
        if x > y:
            print "x is the largest odd number. #4"
        else:
            print "y is the largest odd number. #5"

    elif z_is_odd and not y_is_odd:
        if x < z :
            print "z is the largest number. #6"
        else:
            print "x is the largest number. #7"
    elif not y_is_odd:
        print "x is the largest number. #8" 

elif not x_is_odd:
    if (y_is_odd) and (z_is_odd):
        if y > z :
            print "y is the largest odd number. #9"
        else:
            print "z is the largest odd number. #10"
    elif not y_is_odd:
        if z_is_odd:
            print "z is the largest number. #11" 
        else:
            print "there is no odd number"
    else:
        print "y is the largest number. #12"
    
else:
    print "there is no odd number"
    
print 'end of code'    