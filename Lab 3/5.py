class Account:
    def __init__(self, owner, balance = 0):
    	self.name = owner
    	self.blnc = balance
    def deposit(self, money):
    	if money < 0:
    		return 'Wrong!'
    	self.blnc += money
    	return 'Your balance is ' + str(self.blnc)
    def withdraw(self, money):
    	if self.blnc - money < 0:
    		return 'Wrong!'
    	self.blnc -= money
    	return 'Your balance is ' + str(self.blnc)

x = Account('Name', 123)
print(x.deposit(12))
print(x.withdraw(123))
