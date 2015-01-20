s = 'azcbobobegghakl'
l = len(s)
result = []
for i in range(l+1):
    for v in range(l):
        if 0 < i < len(s):
            if ord(s[l-i-1]) <= ord(s[l-i]):
                if ord(s[l-v]) <= ord(s[l-v+1]):
                    result.append(s[v:i])
while '' in result:
        result.remove('')
        result = sorted(set(result))
print result
print len(result)  