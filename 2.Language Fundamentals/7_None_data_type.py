# None => is creates object.

a = 10 # => creates Object
a = None # => object created by "a = 10" is eligible 

def f1():
	return 10

x = f1()
print('Value returned by f1 :- ',x)

def f1():
	return None

x = f1()
print('Value returned by f1 :- ',x)

def f1():
	print('Hello') # returns Null as defalut.

x = f1()
print('Value returned by f1 :- ',x)
print('Address of x :- ',id(x))
print('Type of x :- ',type(x))

# None creates only one object in PVM for all the variables.
a = None
b = None
c = None

def f1():
	pass

d = f1()

print('Address of a :- ',id(a))
print('Address of b :- ',id(b))
print('Address of c :- ',id(c))
print('Address of d :- ',id(d))

