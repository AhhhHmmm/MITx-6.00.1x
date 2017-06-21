balance = 3926
annualInterestRate = 0.2

def balanceAfterYear(balance, annualInterestRate, monthlyPayment):
	'''
	This function calculates the remaining balance after one year.
	'''
	month = 1
	while month <= 12:
		balance = balance - monthlyPayment
		balance = balance + annualInterestRate/12.0 * balance
		month += 1
	return balance

def payInYear(balance, annualInterestRate):
	monthlyPayment = 0 # start with a monthly payment of 0, which is bound to fail
	finalBalance = balanceAfterYear(balance, annualInterestRate, monthlyPayment)

	# while the final balance is > 0, it means the loan wasn't paid off with the previous
	# so increase the monthly balance by 10 (since this problem must be a multiple of 10)
	# then check if this new amount pays off the balance
	while finalBalance > 0:
		monthlyPayment += 10
		finalBalance = balanceAfterYear(balance, annualInterestRate, monthlyPayment)
	return monthlyPayment, finalBalance

monthlyPayment = payInYear(balance, annualInterestRate)[0]
print('Lowest Payment: {}'.format(monthlyPayment))