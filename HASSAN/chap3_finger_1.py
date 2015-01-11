"""
Write a program that asks the user to enter an integer and
prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
to the integer entered by the user. If no such pair of integers exists, it should
print a message to that effect.

Eliminated the trivial case where root = x and pwr = 1 always exists
"""


def enter_input(x):

	# x = int(input("Enter an integer : "))

	root = 0 
	pwr = 1
	while (pwr < 6) and (root**pwr != x):
		pwr = pwr + 1
		while (root**pwr < x):
			root = root + 1

	if (root ** pwr == x):
		print "There exists a pair " + str(root) + "**" + str(pwr) + " for " + str(x)
	else:
		print "Sorry there isn't any pair!"

		
if __name__ == "__main__":
	enter_input(4)
	enter_input(189)
	enter_input(976)
	enter_input(9)
	enter_input(3444)
