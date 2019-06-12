from os import sys
class Account:
    
    def __init__(self):
        self.current_account = 0
        self.available_account = 0
        self.charge_account = 0
        self.amount_deposited_today = 0
        self.amount_withdrawn_today = 0
        self.withdrawal_frequency = 0
        self.deposit_frequency = 0


class ATM:

    def __init__(self):
        self.account = Account()

    def option_1(user_input = None):
        if user_input == None:
            return ("""
            BALANCE
            {}
            Type "menu" and press enter to go back to main menu
            >
            """).__repr__().replace("\\n","\n")

    def option_2(user_input = None):
        return ("""
        DEPOSIT
        Current Balance: {}
        Error: {}
        Enter amount and press enter (or type menu and press enter to go back to main menu)
        >
        """).__repr__().replace("\\n","\n")

    def option_3(user_input = None):
        return ("""
        WITHDRAWAL
        Current Balance: 150000.00
        Error: {}
        Enter amount and press enter (or type menu and press enter to go back to main menu)
        >
        """).__repr__().replace("\\n","\n")

    def option_4(user_input = None):
        return ("""
        QUIT
        Are you sure you want to quit? (yes/no)
        >
        """).__repr__().replace("\\n","\n")

    def main_menu(self, option = None):
        
        if not option:
            return ("""
            1. Balance
            2. Deposit
            3. Withdrawal
            4. Quit

            Enter Menu option
            > 
            """).__repr__().replace("\\n","\n")
        option = input("Please pick an option: ")
        response_handler(option)
        

    def response_handler(self, option):
        option_submenus = {
            1: self.option_1,
            2: self.option_2,
            3: self.option_3,
            4: self.option_4
        }
        while option != 'yes':            
            return option_submenus[option]()
        return sys.exit

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

    def deposit(self, deposit_amount):
        error = None
        atm_1 = self.max_transaction_frequency("Deposit")   
        if not atm_1['status']:
            return atm_1

        atm_2 = self.max_daily_transaction("Deposit")
        if not atm_2['status']:
            return atm_2

        atm_3 = self.max_transaction_amount("Deposit", deposit_amount)  
        if not atm_3['status']:
            return atm_3
        self.account.current_account += deposit_amount
        self.account.available_account = self.account.current_account
        self.account.deposit_frequency += 1
        error = 'Deposit successful'
        return {'status': True, 'data': error}        

    def balance(self):
        return self.account.available_account

    def withdrawal(self, withdrawal_amount):
        error = None
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
    inst = ATM()
    print(inst.main_menu())