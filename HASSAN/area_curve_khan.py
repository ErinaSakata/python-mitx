"""
This python code implements the Khan Academy's tutorial on
Simple Riemann approximation using rectangles

"""
def f(x):
	return x**2 + 1

def area_curve(start, step, stop):
	""" Assume that you are given f(x), start, stop and step values
	Returns Total area under the curve - it will be underestimated
	"""
	totalarea = 0.0
	while start < stop:
		totalarea = totalarea + f(start)*step

		# print "totalarea : ",totalarea, " for x = ", start
		start += step	
	return totalarea

if __name__ == '__main__':
	print "area = ", area_curve(-10,0.5,3.0)
	print "area = ", area_curve(2,0.5,3.0)
	print "area = ", area_curve(1,0.5,5)
	print "area = ", area_curve(10,0.4,17)
