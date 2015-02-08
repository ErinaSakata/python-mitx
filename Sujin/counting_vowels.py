'''program that counts up the number of vowels contained in the string s. /
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. /
    For example, if s = 'azcbobobegghakl'''
    
# Paste your code into this box 
s = 'azcbobobegghakl'
s = s.lower()
count = 0
for char in s :
    if char in 'aeiou':
        count += 1
print "Number of vowels:",count