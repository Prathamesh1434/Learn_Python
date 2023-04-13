# WAP to get the value  from the dictonary for the given key
k = eval(input('Enter the key => '))
d1 = {100:'A',200:'B',300:'C',400:'A'}
print('d1 => ',d1)
print('Value of key {} => {}'.format(k,d1.get(k,'Not in Dictonary.')))
print()

# WAP to get the value from the dictonary for the given value.
value = input('Enter the value => ')
available = False
for k,v in d1.items():
	if v == value:
		print('The corresponding KEY =>',k)
		available = True

if available == False:
	print('The value not find in the  dictonary.')