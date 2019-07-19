from os import sys


def main_menu():
	print(
		"""
	    1. Balance
	    2. Deposit
	    3. Withdrawal
	    4. Quit
	
	    Enter Menu option
	    > 
    """)
	option = str(raw_input("Choose an option:"))
	if option == "1":
		balance()
	elif option == "2":
		deposit()
	elif option == "3":
		withdrawal()
	elif option == "4":
		handle_end()
	else:
		print ("Invalid option, Try Again")


def handle_end():
	exit(0)
	return


def charges(self, amount):
	pass


def max_transaction_frequency(self, transaction):
	error = None
	if transaction == "Deposit":
		if self.account.deposit_frequency == 4:
			error = "You have reached your deposit frequency"
			print(error)
			return {'status': False, 'data': error}
	elif transaction == "Withdrawal":
		if self.account.withdrawal_frequency == 3:
			error = "You have reached your deposit frequency"
			return {'status': False, 'data': error}
	return {'status': True, 'data': error}


def max_transaction_amount(self, transaction, transaction_amount):
	error = None
	if transaction == "Deposit":
		if transaction_amount > 40000:
			error = "You cannot deposit more than 40,000 per transaction"
			return {'status': False, 'data': error}
	if transaction == "Withdrawal":
		if transaction_amount > 20000:
			error = "You cannot withdraw more than 20,000 per transaction"
			return {'status': False, 'data': error}
	return {'status': True, 'data': error}


def max_daily_transaction(self, transaction):
	error = None
	if transaction == "Deposit":
		if self.account.amount_deposited_today >= 150000:
			error = "You have reached your allowed daily maximum withdrawal amount"
	if transaction == "Withdrawal":
		if self.account.amount_withdrawn_today >= 50000:
			error = "You have reached your allowed daily maximum withdrawal amount"
			return {'status': False, 'data': error}
	return {'status': True, 'data': error}


def sufficient_funds(self, withdrawal_amount):
	error = None
	if withdrawal_amount > self.account.available_account:
		error = "You have insufficient funds. Available amount: {}".format(self.account.available_account)
		return {'status': False, 'data': error}
	return {'status': True, 'data': error}


def atomicity_check(self, transaction, amount):
	error = None
	if transaction == "Deposit":
		self.max_transaction_frequency("Deposit")
		self.max_daily_transaction("Deposit")
		self.max_transaction_amount("Deposit", amount)
	if transaction == "Withdrawal":
		self.max_transaction_frequency("Withdrawal")
		self.max_daily_transaction("Withdrawal")
		self.max_transaction_amount("Withdrawal")
		self.sufficient_funds(amount)


def deposit():
	global deposit_total
	global deposit_frequency
	global available_account
	amount = float(raw_input("Enter the amount you want to deposit: "))
	if deposit_frequency + 1 > 4:
		print("You have reached maximum deposit frequencies for the day.Try again tomorrow")
		return
	if (amount + deposit_total) > 150000:
		print("You have reached maximum deposit amount for the day.Try again tomorrow")
		return
	if amount > 60000:
		print("You Are above the Maximum Transactional Limit.Maximum limit is 60,000")
		return
	deposit_total += amount
	deposit_frequency += 1
	available_account += amount
	print('[ You have Successfully deposited: %s]\n\n' % amount)
	print('[ New Account Balance: %s]\n\n' % available_account)
	return True


def balance():
	global available_account
	print "[Your current balance is:]", available_account
	return


def withdrawal():
	atm_1 = self.max_transaction_frequency("Withdrawal")

	if not atm_1['status']:
		return atm_1
	atm_2 = self.max_daily_transaction("Withdrawal")
	if not atm_2['status']:
		return atm_2
	atm_3 = self.max_transaction_amount("Withdrawal", withdrawal_amount)
	if not atm_3['status']:
		return atm_3
	atm_4 = self.sufficient_funds(withdrawal_amount)
	if not atm_4['status']:
		return atm_4
	self.account.available_account -= withdrawal_amount
	self.account.current_account = self.account.available_account
	self.account.withdrawal_frequency += 1
	error = "Withdrawal successful"
	return {'status': True, 'data': error}


if __name__ == "__main__":
	current_account = 0
	available_account = 0
	charge_account = 0
	amount_deposited_today = 0
	amount_withdrawn_today = 0
	withdrawal_frequency = 0
	deposit_frequency = 0
	deposit_total = 0.00
	while True:
		main_menu()
