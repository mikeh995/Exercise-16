class Account:
    number_Created = 0
    Deposits = 0

    def __init__(self, initial):
        self._balance = initial
        Account.number_Created += 1
        Account.Deposits += initial
    def deposit(self, amt):
        self._balance += amt
        Account.Deposits += amt

    def withdraw(self,amt):
        self._balance -= amt
        Account.Deposits -= amt

    def getbalance(self):
        return self._balance

    def add_interest(self, interest):
        pass

    def __str__(self):
        return f"Account id: ${self.getbalance()}"

    def __gt__(self, other):
       return self._balance > other.getbalance()

    def __lt__(self, other):
       return self._balance < other.getbalance()

    @classmethod
    def get_total_balance(cls):
        return f"The Royal Bank of Papua New Guinea has reserves of:  ${cls.Deposits}"