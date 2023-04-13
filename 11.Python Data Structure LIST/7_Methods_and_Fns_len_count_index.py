# len() , count() , index()
l = [10,20,30,7]
print('Length of l => ',len(l))

l.append(10) # Only for list object.

print('Soreted list l1 => ',sorted(l))

l = [10,20,10,20,30,20,40]

print('Count of 10 in l1  => ',l.count(10))
print('Count of 20 in l1  => ',l.count(20))
print('Count of 50 in l1  => ',l.count(50))

l = [1,2,1,2,3,4]
print('first occourance index of 1 in list l => ',l.index(1))
print('first occourance index of 2 in list l => ',l.index(2))
# print('first occourance index of 5 in list l => ',l.index(5)) => if element is not available in the list , it will give error.

print()

l = [1,2,2,2,3,3]
x = int(input('Enter element to find => '))

if x in l:
	print('first occourance index of {} in list l => {}'.format(x,l.index(x)))
else:
	print(x,'is not availble in list.')