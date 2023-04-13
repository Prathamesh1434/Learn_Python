# print(__name__)

if __name__ == '__main__':
	print('Direct execution like main program.')
else:
	print('indirect execution due to import statement.')

def f1():
	print('f1 Execution.')

def f2():
	print('f2 Execution.')

def f3():
	print('f3 Execution.')

if __name__ == '__main__':
	f1()
	f2()
	f3()