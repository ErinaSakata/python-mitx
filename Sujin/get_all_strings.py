 # get all strings into list
s = 'abcbcd'
result = []

for i in range(len(s)+1):
    for v in range(len(s)):
        result.append(s[v:i])
    while '' in result:
        result.remove('')
        result = sorted(set(result))
#print result
print result
print "Number of the list :", len(result)
