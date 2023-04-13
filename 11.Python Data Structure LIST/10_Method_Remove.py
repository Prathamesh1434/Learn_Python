# remove()
# it will remove 1st occourance.
# if element is not avaliable , then it will value error.

l = [10,20,10,20,40]

print('List before remove 40 => ',l)
l.remove(40)
print('List before after 40 => ',l)

l.remove(10)
print('List before after 10 => ',l)

print()

# l.remove(50) => it will give value error as it is not the part of list l.

l = [1,2,3,4,5,6]
print('l before removal => ',l)

x = int(input('Enter element to remove => '))

if x in l:
	l.remove(x)
	print('l after removal => ',l)
else:
	print(x,'is not present in list.')

print()

# How to remove all occourance ?
l = [1,1,1,1,2,2,2,3,3]
print('l before removal => ',l)
x = int(input('Enter element to remove => '))
while True:
	if x in l:
		l.remove(x)
	else:
		break
print('l after removal => ',l)