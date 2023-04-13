a = 10 # Global variable

def f1():
	a=20 # Local variable
	print('a= ',a) # a = 20

def f2():
	print('a= ',a) # a = 10

f1()
f2()
print()

# golbal keyword
# 1 To make the global variable avaliable to fn , so we can do the required modification.
def f3():
	global a
	a=20 # It will change the value of global variable.
	print('a= ',a) # a = 20

def f4():
	print('a= ',a)

f3()
f4()
print()

# 2 To declare the global variable inside the function.
def f5():
	global b # It will make variable to to the global , so it can access outside the fucntion.
	b=20 # Local variable
	print('b= ',b) # a = 20

def f6():
	print('b= ',b) # a = 10

f5()
f6()
print()