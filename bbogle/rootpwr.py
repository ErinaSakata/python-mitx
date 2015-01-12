msg = "Sorry, You must Enter a integer number"
while True:
    root = int(raw_input('Enter a number of root : '))

    if type(root) != int:
        print msg

    pwr = int(raw_input('Enter a number of pwr, 0 ~ 6 : '))

    if type(pwr) != int:
        print msg
    elif not (0 < pwr < 6):
        print 'Sorry, pwr number 0 ~ 6'

    if type(root) == int and type(pwr) == int and 0<pwr<6:
        break

print str(root) + '**' + str(pwr) + ' = ' + str(root**pwr)
