# Nested List
l = [10,20,[30,40]]
print('Element at 0 => ',l[0])
print('Element at 1 => ',l[1])
print('Element at 2 => ',l[2])

print()

print('Element at 3 and sub element at 0 => ',l[2][0])
print('Element at 3 and sub element at 1 => ',l[2][1])

print()

# Nested list as Matrix
l = [[10,20,30],[40,50,60],[70,80,90]]
print(l)
print('Elements row wise => ')
for x in l:
	print(x)

print('Elements in Matrix Style :')
for x in l:
	for y in x:
		print(y,end=' ')
	print()