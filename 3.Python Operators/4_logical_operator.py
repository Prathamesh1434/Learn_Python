# and , or , not

# 1. For boolean type
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

print('-----------------------------')

username = input('Enter Username :- ')
password = input('Enter password :- ')

if username == 'Prathmesh' and password == 'Babalu' :
	print('Valid User.')
else:
	print('Invalid User.')

print('-----------------------------')

# 2. For non-boolean type

# 0 / empty String,List,Set,Tuple,dict = False
# Non-Zero / Non-Zero tring,List,Set,Tuple,dict = True

# a. 'and' Operator
print(10 and 20) # => x is true => y is the result.
print(0 and 20) # => x is false => x is the result.

print('Prathmesh' and 'Dnyanesh') # => x is true => y is the result.
print('' and 'Dnyanesh') # => x is false => x is the result.

# b. 'or' Operator
print(10 or 20) # => x is true => x is the result.
print(0 or 20) # => x is false => y is the result.

print('Prathmesh' or 'Dnyanesh') # => x is true => x is the result.
print('' or 'Dnyanesh') # => x is false => y is the result.
print([] or 'Prathmesh')

# c. 'not' Operator

# The result is always boolean.
print(not 'durga')
print(not '')
print(not 10)
print(not 0)







