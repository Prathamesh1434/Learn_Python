# Ordering elements of list.

# Reversing Oreder:
# reverse() => List specific
l = [10,20,30,40]
print('List before reverse => ',l)
l.reverse()
print('List after reverse => ',l)

print()

# reversed() => Python inbult function
l = [10,20,30,40]
print('List before reversed => ',l)
r = reversed(l)
print('Type of r => ',type(r))
l1 = list(r)
print('List after reversed => ',l1)

s = 'Prathmesh'
print('String before reversed => ',s)
r = reversed(s)
for x in r:
	print(x)