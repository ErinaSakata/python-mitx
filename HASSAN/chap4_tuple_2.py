"""
Find extreme divisors of n1 and n2
use temp variables minValue and maxValue 
"""

list1 = [1,2,3,4]
list2 = [1,2,5,6]
list3 = list1[:]
for e1 in list1:
	if e1 in list2:
		list3.remove(e1)

print list1
print list3

