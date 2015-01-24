"""
Explanation of list objects 
"""

Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs,Ivys]
Univs1 = [['MIT', 'Caltech',"Cornell"], ['Harvard', 'Yale', 'Brown']]

print Univs1 == Univs

print "Univs1 = ", Univs1 , " id : " , id(Univs)
print "Univs = ", Univs , " id : " , id(Univs1)