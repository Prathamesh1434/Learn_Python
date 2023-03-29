# replace old string with replace() method
# s.replace(oldString,newString)
s = 'ABABABA'
s1 = s.replace('A','B')
print('String After replacement => ',s1)

s = 'Prathmesh Jayant Gayakwad'
s1 = s.replace(' ','')
print('String After replacement => ',s1)
print('The number of spaces in s => ',s.count(' '))
print('The number of spaces in s => ',len(s)-len(s1))

# replace() method is case sensitive.

# String objects are immutable , then how we can change the content by using replace() method ?
s = 'ABABABA' # s => ABABABA
s1 = s.replace('A','B') # s1 => BBBBBBB
print('String s => ',s)
print('String After replacement => ',s1)

s = 'ABABABA' # s => ABABABA
print('String s before replacement with Address ID {} => '.format(id(s)),s)
s = s.replace('A','B') # s => BBBBBBB => and object 'ABABABA' will be available for garbage collection.
print('String s after replacement with Address ID {} => '.format(id(s)),s)

# split() and join() method for splitting and joining the the string.
s = 'Prathmesh Jayant Gayakwad'
l = s.split() # default seprator is space ' '.
print(l)

for x in l:
	print(x)

d = '05-04-2019'
l = d.split('-')
for x in l:
	print(x)

# joining the string
l = ['Prathmesh','Jayant','Gayakwad']
s = ' '.join(l) # Sperator.join(l)
print('result after joining all the values from list l => ',s)

s = '-'.join(l) # Sperator.join(l)
print('result after joining all the values from list l => ',s)

s = ''.join(l) # Sperator.join(l)
print('result after joining all the values from list l => ',s)

l = ['05','04','2019']
s = '-'.join(l) # Sperator.join(l)
print('result after joining all the values from list l => ',s)

s = '/'.join(l) # Sperator.join(l)
print('result after joining all the values from list l => ',s)










