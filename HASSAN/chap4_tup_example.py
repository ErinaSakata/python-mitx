"""
Find all divisors of two numbers n1 and n2, and return result as tuple
"""

def findDivisor(n1,n2):
	divisors = ()

	for i in range(1, min(n1,n2) +1):
		if n1%i == 0 and n2%i == 0:
			divisors = divisors + (i,)

	return divisors

answer = findDivisor(20,100)
print answer

for s in answer:
	print s
