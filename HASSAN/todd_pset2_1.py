# Paste your code into this box
monthlyInterestRate = annualInterestRate/12.0
paid = 0.0

for i in range (12):
	print "Month: ", (i+1)
	minimum = monthlyPaymentRate * balance
	paid = paid + minimum
	print "Minimum monthly payment: ", round(minimum,2)
	balance = balance - minimum
	balance = balance + (monthlyInterestRate * balance)
	print  "Remaining balance: ", round(balance,2)

print "Total paid: ", round(paid,2)
print "Remaining balance: ", round(balance,2)

monthlyInterestRate = annualInterestRate/12.0
TotalPaid = 0


for month in range(1,13):
    minimumPaid = monthlyPaymentRate * balanace
    TotalPaid = TotalPaid + minimumPaid
    balance = (balance - minimumPaid)
    balance = balance + (monthlyInterestRate * balance )
    print "Month: %s" % (month) 
    print "Remaining Balance: %s" % (round(remainingBalance, 2))
    print "Minimum Monthly Payment: %s" % (round(monthlyPaymentRate, 2))
    
print "Total paid: %s"  % (round(TotalPaid, 2))
print  "Remaining Balance:%s" % (round(balance, 2))