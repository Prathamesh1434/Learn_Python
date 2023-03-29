# python specific terminology 
# we can use it for empty block

def f1():
	pass # Empty body

class A:
	pass # Empty body

class B:
	pass # Empty body

class C:
	pass # Empty body

x = int(input("Enter marks :- "))
if x > 35:
	print('Success.')
else:
	pass # This pass may get replace with the statement that we want to execute in the future.

# Ex => Abstract method => Method without body.

from abc import *
class Loan(ABC):
	@abstractmethod
	def getInterestRate(self):
		pass

class HomeLoan(Loan):
	def getInterestRate(self):
		return 8;

class VehicleLoan(Loan):
	def getInterestRate(self):
		return 10;

h = HomeLoan()
print('Interest Rate for HomeLoan :- ',h.getInterestRate())

v = VehicleLoan()
print('Interest Rate for VehicleLoan :- ',v.getInterestRate())	

# To define minimal class we use 'pass'.
class A:
	pass

# To define minimal function we use 'pass'.
def b():
	pass