from main import ATM

class TestATM:

    def test_balance(self):
        atm = ATM()
        atm.account.available_account = 1000
        assert atm.balance() == 1000

    def test_max_transaction_frequency(self):
        atm = ATM()
        assert atm.max_transaction_frequency("Deposit")['data'] == None
        assert atm.max_transaction_frequency("Withdrawal")['data'] == None
        atm.account.deposit_frequency = 4
        atm.account.withdrawal_frequency = 3
        assert atm.max_transaction_frequency("Deposit")['data'] == "You have reached your deposit frequency"
        assert atm.max_transaction_frequency("Withdrawal")['data'] == "You have reached your deposit frequency"

    def test_max_transaction_amount(self):
        atm = ATM()
        assert atm.max_daily_transaction("Withdrawal")["data"] == None
        assert atm.max_daily_transaction("Withdrawal")["data"] == None
        atm.account.amount_deposited_today = 150000
        atm.account.amount_withdrawn_today = 50000
        assert atm.max_daily_transaction("Withdrawal")["data"] == "You have reached your allowed daily maximum withdrawal amount"
        assert atm.max_daily_transaction("Deposit")["data"] == "You have reached your allowed daily maximum withdrawal amount"

    def max_transaction_amount(self):
        atm = ATM()
        assert atm.max_transaction_amount("Deposit", 4000) == None
        assert atm.max_transaction_amount("Withdrawal", 500) == None
        assert atm.max_transaction_amount("Deposit", 60000) == "You cannot deposit more than 40,000 per transaction"
        assert atm.max_transaction_amount("Withdrawal", 60000) == "You cannot withdraw more than 20,000 per transaction"

    def test_suficient_funds(self):
        atm = ATM()
        atm.account.available_account = 2000
        assert atm.sufficient_funds(1000)["data"] == None
        assert atm.sufficient_funds(5000)["data"] == "You have insufficient funds. Available amount: 2000"

    def test_deposit(self):
        atm = ATM()
        assert atm.deposit(1000)['status'] == True
        atm.account.amount_deposited_today = 40000

    def test_withdrawal(self):
        atm = ATM()
        atm.account.available_account = 5000
        assert atm.withdrawal(2000)['status'] == True
        atm.account.amount_withdrawn_today = 20000
       