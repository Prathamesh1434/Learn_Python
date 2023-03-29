# transfer statement

#1. 'break' statement

for i in range(10):
	print(i)
	if i == 3:
		print("Processing is done . Loop breaked.")
		break

print('Outside of loop.')

print()

# Ex
cart=[10,20,30,5000,600,750,80]

for item in cart:
	if item > 500:
		print("to place the order of rs '{}' insurance must be required , we can't proceed further.".format(item) )
		break
	print('Item purchesed of rs {}.'.format(item))

print()

#Ex => following condition is not possible , 'break' statement should be used inside the loop.
# x = 10
# if x > 40:
# 	print('Stop the program.')
# 	break
# print("Hello")

# 2. 'continue' statement

for i in range(10):
	if i%2==0:
		continue
	print(i)

print()

cart=[10,20,30,5000,600,750,80]

for item in cart:
	if item > 500:
		print("to place the order of rs '{}' insurance must be required .".format(item) )
		continue
	print('Item purchesed of rs {}.'.format(item))

print()
# Ex
l = [10,20,0,5,0,30]

for i in l:
	if i == 0:
		print("we can't divide 100 by 0.")
		continue
	print('100/{} = {}'.format(i,100//i))

#Ex => following condition is not possible , 'continue' statement should be used inside the loop.
# x = 10
# if x > 40:
# 	print('Stop the program.')
# 	continue
# print("Hello")