# Traversing elements of the list
l = [0,1,2,3,4,5,6,7,8,9,10]

# 1 => By using while loop
i = 0
while i < len(l):
	print(l[i])
	i = i+1

# 2 => By using for loop
for x in l:
	print(x)

# 3 => only even numbers
for x in l:
	if x%2==0:
		print(x)

i = 0
while i < len(l):
	print('The element present at +ve index:{} and -ve index:{} => {}'.format(i,i-len(l),l[i]))
	i += 1

