# global keyword
a = 777
def f1():
	# print('a= ',a) => SyntaxError: name 'a' is used prior to global declaration
	global a
	print('a= ',a)
	a = 999
	print('a= ',a)

f1()

b = 888
def f2():
	b = 111
	print('b= ',b)
	print('Global value of variables b =>',globals().get('b'))
	print('Global value of variables a =>',globals()['a'])
	print('Dictonary of variables =>',globals())

f2()