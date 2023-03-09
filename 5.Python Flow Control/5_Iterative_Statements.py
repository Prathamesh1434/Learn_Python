# 1. for loop

# for x in sequence:
# 	Activity

s = 'Sunny Leone'
i = 0
for x in s:
	print('The char present at {} index : {}'.format(i,x))
	i = i  + 1
	# i += 1


s = input('Enter String : ')
i = 0
for x in s:
	print('The char present at {} index : {}'.format(i,x))
	i = i  + 1
	# i += 1

# Application

# range(n) => 0 to n - 1
# range(m,n) => m to n-1
# range(m,n,inc/dec) => m to n-1 with inc or dec.

for x in range(10):
	print('Hello , Welcome to python for loop.')


for x in range(1,11):
	print(x)

# odd number from 0 to 20
for x in range(21):
	if x%2 != 0:
		print('odd number : ',x)

for x in range(1,21,2):
	print('odd number : ',x)

# To display numbers 10 to 1 in decending order
for x in range(10,1,-1):
	print(x)

# To print the sum of numbers in the given list:
list = eval(input("Enter list of numbers : "))

print('Direct Sum of elements of list : ',sum(list))
sum = 0

for x in list:
	sum = sum + x

print('The Sum:',sum)



# 2. while loop

# while condition:
# 	body

i = 1

while i <= 10:
	print('Hello , Welcome to while loop.')
	i = i+1

i = 1

while i<=10:
	print(i)
	i = i + 1

# TO print numbers from 1 to 20 , which are divisible by 3
x = 1

while x <= 20:
	if x%3==0:
		print('divisible by 3 = ',x)
	x += 1

# WAP to display sum of 1st n numbers.
n  = int(input('Enter Number : '))

sum = 0
i = 1

while i<=n:
	sum = sum + i
	i += 1

print('The sum :- ',sum)

# 
name = ''

while name != 'Sunny':
	name = input('Enter the name of your favourite actress: ')

print('Thanks for confirmation.')























