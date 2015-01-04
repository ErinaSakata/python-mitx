# -*- coding: utf-8 -*-
print ("구구단을 출력합니다.")

for x in range(2, 10):
    print ("------------- [" + str(x) + "단] -----------------")
    for y in range(1,10):
        print (str(x)+" * "+str(y)+" = "+str(x*y))
    print ("--------------------------------------------------")

raw_input("press<enter>")    
