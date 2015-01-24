def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    
def radiation(start,stop,step):
    stop1 = float(stop)
    start1 = float(start)
    step1 = float(step)
    totalexp = stop1 - start1 # gets the diff (total time exposed)
    numofrects = [] #makes an empty list to count how many 'rects'
     # to be able to append a list
    while stop1 >= start1: #making a list
        start1 += step1
        numofrects.append(start1)
        
        
    totalarea = 0  #declare total area
    for x in numofrects:

        area = f(x) * step1
        totalarea += area
    print stop, stop1, start, start1, step, step1
    return totalarea
        
print radiation(0, 5, 1)