def f(x):
	return x**2 + 1

def area_curve(start, step, stop):
	totalarea = 0.0
	while start < stop:
		totalarea = totalarea + f(start)*step

		print "totalrea : ",totalarea, " for x = ", start
		start += step	
	return totalarea

if __name__ == '__main__':
	print area_curve(-10,0.5,3.0)