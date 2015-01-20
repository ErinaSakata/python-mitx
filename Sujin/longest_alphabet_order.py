# get all strings into list
s = 'azcbobobegghakl'
result = []
count = 0
for i in range(len(s)+1):
    for v in range(len(s)):
        if 0 < i < len(s) and 0 <= v < len(s)-1:
            if ord(s[len(s)-i-1]) <= ord(s[len(s)-i]):
                s[len(s)-i-1:len(s)-i+1]
                result.append(s[v:i])
while '' in result:
    result.remove('')
    result = sorted(set(result))
#print result
print result
print "Number of the list :", len(result)
print max(result, key=len)

