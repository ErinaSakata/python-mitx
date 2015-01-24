"""
some examples of dictionaries
"""
newdict = dict()
newlist = list()
idnName = {'Hassan' : 1, 'Sujin' : 2, 'Rachell' : 3, 'Olga' : 4, 'Jaeho' : 5, (6,3) : 'Unknown'}

# print idnName['SUjin']
# print idnName.get('Sujin', 'not found')
# print idnName[(6,3)]

# print idnName.keys()

# keys = []
# for e in idnName:
# 	keys.append(e)
# keys.sort()
# print "keys : " , keys

# print len(idnName)

listMeaning = ['Go', 'Come', 'Sleep']

for val in range(len(listMeaning)):

	if listMeaning[val] == "Come":
		print "found it"


