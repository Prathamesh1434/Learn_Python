# Types of variables:
# 1 Global Variables
# 2 Local Variables

a = 10 # Global variable
def f1():
	print('a =>',a)

def f2():
	print('a =>',a)

f1()
f2()

def f3():
	b = 10 # Local Variable
	print('b =>',b)

def f4():
	pass
	# print('b =>',b) => NameError: name 'b' is not defined

f3()
f4()