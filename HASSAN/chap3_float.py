"""
Comparing two float numbers

"""

x = 0.0
for i in range(10):
	x = x+0.1
	# print "x : ",x
	# x = round(x,1)
if x == 1.0:
# if abs(x-1.0) < 0.0001:
	print x," = 1.0"
else:
	print x, "is not 1.0"