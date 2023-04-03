from accountinfo import Account

George_Agdgdgwenge = Account(1234000000.01)
George_Agdgdgwenge.deposit(9992.76)
George_Agdgdgwenge.deposit(87465.32)
George_Agdgdgwenge.withdraw(22200.22)

print(George_Agdgdgwenge)


Mike = Account(10000)
Mike.deposit(4.02)
Mike.deposit(234)
Mike.withdraw(3.20)

print(Mike)
print(Mike.getbalance())

Amiee = Account(2000)
Amiee.deposit(500)
Amiee.deposit(50)
Amiee.deposit(40)
Amiee.withdraw(22)

print(Amiee)
print(Amiee.getbalance())

print('Number of accounts created', Account.number_Created)
print(George_Agdgdgwenge.get_total_balance())