# import time so you can time the program
import time

# set start time of program for timing purposes
start = time.time()

balance = 320000
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
	# If the abs(amount) in the account is less than 1 cent then that means the loan
	# is completely paid off with no extra paid off. Epsilon is the threshold for this.
	epsilon = 0.01

	# Set initial minimum and maximum values for binary search.
	minMonthlyPayment = balance / 12.0
	maxMonthlyPayent = balance * (1 + annualInterestRate / 12.0)**12/12.0

	# Set monthly payment to the average of the two boundaries and then commence binary serach
	monthlyPayment = (minMonthlyPayment + maxMonthlyPayent) / 2.0
	finalBalance = balanceAfterYear(balance, annualInterestRate, monthlyPayment)

	# Check if you over paid or under paid. Recalibrate bounds based on this and re-average bounds
	# to get the next possible monthly payment.
	while abs(finalBalance) > epsilon:
		if finalBalance > 0:
			minMonthlyPayment = monthlyPayment
		elif finalBalance < 0:
			maxMonthlyPayent = monthlyPayment
		monthlyPayment = (minMonthlyPayment + maxMonthlyPayent) / 2.0
		finalBalance = balanceAfterYear(balance, annualInterestRate, monthlyPayment)
	return monthlyPayment, finalBalance

monthlyPayment = round(payInYear(balance, annualInterestRate)[0],2)
print('Lowest Payment: {}'.format(monthlyPayment))

# set end time of program for timing purposes
end = time.time()

# total time to run is the difference beteen start and end time.
print(end - start)
