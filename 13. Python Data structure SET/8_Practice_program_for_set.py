l = eval(input("Enter the list with duplicate => "))
print('list l =>',l)
s = set(l)
l1 = list(s)
print('List without dupliate =>',l1)

l1 = []
for x in l:
	if x not in l1:
		l1.append(x)

print('List without dupliate =>',l1)

# Write a program to print different vowels present in the given word ?
word = input('Enter the string => ')
print('String =>',word)
s = set(word)
v = {'a','e','i','o','u'}
result = s.intersection(v) # s&v
print('Vowels in the string => ',sorted(result))