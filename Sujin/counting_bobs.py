'''Write a program that prints the number of times the string 'bob' occurs in s.\
For example, if s = 'azcbobobegghakl', then your program should print
'''

# Paste your code into this box

num = len(s)
count = 0
for i in range(num - 3):
    if s[i:i+3] == 'bob':
        count += 1
print "Number of times bob occurs is: ", count
