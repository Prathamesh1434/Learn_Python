# 1. EX
a = int(input('Enter First Number :- '))
b = int(input('Enter Second Number :- '))

if a > b:
	print("Greater Number : ",a)
else:
	print("Greater Number : ",b)

# 2. EX
a = int(input('Enter First Number :- '))
b = int(input('Enter Second Number :- '))
c = int(input('Enter Third Number :- '))

if a > b and a > c:
	print("Greater Number : ",a)
elif b > c:
	print("Greater Number : ",b)
else:
	print("Greater Number : ",c)

# 3. EX : WAP to check weather the given number is in between 1 and 100 or not ?
a = int(input('Enter First Number :- '))

if a >= 1 and a <= 100:
	print('The Number {} is in between 1 and 100.'.format(a))
else:
	print('The Number {} is not in between 1 and 100.'.format(a))