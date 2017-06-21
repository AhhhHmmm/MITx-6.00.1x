balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def futureBalance(balance, annualInterestRate, monthlyPaymentRate, totalTime):
	'''
	Inputs:
	balance: initial balance in the account (float)
	annualInterestRate: interest rate as decimal (float)
	monthlyPaymentRate: monthly payment rate as decimal (float)
	totalTime: time leaving money in the account in months (integer, float)

	Outputs:
	returns the balance after 12 months (float)
	'''
	month = 1
	while month <= totalTime:
		balance = balance - monthlyPaymentRate*balance
		balance = balance + annualInterestRate / 12.0 * balance
		balance = round(balance, 2)
		# print('Month {} Remaining balance: {}'.format(month, balance))
		month += 1
	return balance

reaminingBalance = futureBalance(balance, annualInterestRate, monthlyPaymentRate, 12)
print('Remaining balance: {}'.format(reaminingBalance))