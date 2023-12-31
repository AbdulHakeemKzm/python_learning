
class Account:


	def __init__(self, filepath):
		self.filepath = filepath
		with open(filepath, 'r') as file:
			self.balance=int(file.read())
	
	def withdraw(self, amount):
		self.balance=self.balance - amount
		
	def deposit(self, amount):
		self.balance=self.balance + amount
	
	def commit(self):
		with open(self.filepath, 'w') as file:
			file.write(str(self.balance))
			
class Checking(Account):

	"""This class generates checking account objects"""
	
	type="checking"
	
	def __init__(self, filepath, fee):
		Account.__init__(self, filepath)
		self.fee = fee
		
	def transfer(self, amount):
		self.balance = self.balance - amount - self.fee
		
checking = Checking("balance.txt", 100)
checking.transfer(100)
checking.deposit(2000)
print(checking.balance)
checking.commit()
print(checking.type)

checking1 = Checking("balance 1.txt",0)
checking1.transfer(100)
print(checking1.balance)
checking1.commit()
print(checking1.type)

print(checking.__doc__)

		
#account=Account("balance.txt")
#print(account.balance)
#account.withdraw(100)
#account.deposit(500)
#print(account.balance)
#account.commit()
