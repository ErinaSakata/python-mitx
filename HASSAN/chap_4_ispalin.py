def isPalin(s):
	""" Assumes s is a str
	Returns True if the letters in s form a palindrome;
	False otherswise; 
	"""
	def toChars(s):
		s = s.lower()
		letters = ''
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				letters = letters + c
		return letters

	def isPal(s):
		if len(s) <=1 :
			return True
		else:
			print "s[0]= ",s[0], " s[-1]= ",s[-1], " isPal: ",isPal(s[1:-1])
			answer = 
			return s[0] == s[-1] and isPal(s[1:-1])

	return isPal(toChars(s))


if __name__ == '__main__':
	print isPalin('saas')