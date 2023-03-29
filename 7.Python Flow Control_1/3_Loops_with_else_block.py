# if the loop executed without 'break' statement , then else part will be executed.

# Ex
cart =[10,20,30,40]

for item in cart:
	if item > 500:
		print("to place the order of rs '{}' insurance must be required , we can't proceed further.".format(item) )
		break
	print('Item purchesed of rs {}.'.format(item))
else:
	print('All items purchesed successfully !')

# else part is not releated with 'else' , it will always get execute.
cart =[10,20,30,40,900,30]

for item in cart:
	if item > 500:
		print("to place the order of rs '{}' insurance must be required , we can't proceed further.".format(item) )
		continue
	print('Item purchesed of rs {}.'.format(item))
else:
	print('All items purchesed successfully !')