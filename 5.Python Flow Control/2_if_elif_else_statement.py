# 1. 'if' statement

if 10 < 20:
	print('10 is less than 20')
print('End of programm')

# Ex
name = input('Enter Name :- ')

if name == 'Prathmesh':
	print('Hello Prathmesh , Good Morning !')
print('How are you ?')

print()

# 2. 'if-else' statement

if name == 'Prathmesh':
	print('Hello Prathmesh , Good Morning !')
else:
	print('Hello Guest , Good Morning !')
print('How are you ?')

# 3. 'if-elif-else' statement

brand = input('Enter your Fav brand :- ')

if brand == 'KF':
	print('It is childrens brand.')
elif brand == 'KO':
	print('It is to light.')
elif brand == 'RC':
	print('Not that much kick.')
elif brand == 'FO':
	print('Buy one get one print.')
else:
	print('Other brands are not recommanded.')

