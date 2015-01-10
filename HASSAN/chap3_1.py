"""Returns the perfect cube root of an integer x

if x is not perfect square then it displays a message 
	
"""

def cube_root(x):

	# x = int(raw_input("Enter integer : "))
	ans = 0

	while ans**3 < abs(x):
		ans = ans + 1

	if ans**3 != abs(x):
		print x, "is not perfect cube"
	else:
		if x < 0:
			ans = -ans

		print "Cube root of", x," is : ",ans


if __name__ == "__main__":
	cube_root(10)
	cube_root(5)
	cube_root(9)
	cube_root(27)
	cube_root(7406961012236344616)