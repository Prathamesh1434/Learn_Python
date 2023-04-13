# append()
l = []
l.append(10)
l.append(20)
l.append(30)
print('List l => ',l)

# add numbers which are devisible 10 to the list from 1 to  100.
l = []
for i in range(1,101):
	if  i%10==0:
		l.append(i)
print('List l => ',l)

# insert() => Add at specified position.
l = [10,20,30,40]
print('List l => ',l)
l.insert(1,55)
print('List l after change => ',l)

l = [10,20,30,40] # valid index => 0 to 3 , -1 to -4

l.insert(100,7777) # it will add 7777 at last.
l.insert(-100,9999) # it will add 9999 at first place.
print('List l after change => ',l)