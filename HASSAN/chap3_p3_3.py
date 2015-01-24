"""

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in 
alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your 
program should print

Longest substring in alphabetical order is: abc
"""

def longest_string(s):
	s = s.lower()

	if len(s) == 0 or len(s) == 1:
		return "No need to go further - " + str(s)

	