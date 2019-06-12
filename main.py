class ATM:

    def __init__(self):
        self.account = Account()

    def charges(self, amount):
        pass

    def menu(option = None):
        if not option:
            return """
            1. Balance
            2. Deposit
            3. Withdrawal
            4. Quit

            Enter Menu option
            > 
            """ 

    def deposit(self, deposit_amount):
        if self.account.amount_deposited_today > 150000 or deposit_amount > 40000 or account.deposit_frequency == 4:
            return "Sorry, you have reached your allowed daily maximum deposit amount"
        if not int(deposit_amount):
            return "Please enter a number"
        self.account.current_account += deposit_amount
        self.account.deposit_frequency += 1
        return "Deposit successful"
        

    def balance(self):
        return self.account.available_account

    def withdrawal(self, withdrawal_amount):
        if self.account.amount_withdrawn_today > 50000 or withdrawal_amount > 20000 or self.account.withdrawal_frequency == 3:
            return "You have reached your daily allowed daily maximum withdrawal amount"
        if not int(withdrawal_amount):
            return "Please enter a number"
        if self.account.available_account > withdrawal_amount:
            return "You have insufficient funds. Available amount: {}".format(self.account.available_account)
        self.account.available_account -= withdrawal_amount
        self.account.withdrawal_frequency += 1
        return "Withdawal successful"

class Account:

    def __init__(self):
        self.current_account = 0
        self.available_account = 0
        self.charge_account = 0
        self.amount_deposited_today = 0
        self.amount_withdrawn_today = 0
        self.withdrawal_frequency = 0
        self.deposit_frequency = 0

if __name__ == "__main__":
    pass