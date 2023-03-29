#1. print * n times with having space between them.

n = int(input('Number of stars required : '))

# Mine
for x in range(n):
	print('*',end=(' '))

print()
print()


#2. Create square of * with the input from keyboard.

# Mine
for x in range(n):
	i = 0
	while i<n:
		print('*',end=(' '))
		i += 1
	print()

print()

# Tutorial
for x in range(n):
	print('* '*n)

print()

#3. print the number from 0 to n , n times in each seprate row.

# Mine
for x in range(n):
	i = 0
	for i in range(n):
		print('{}'.format(x+1),end=' ')
	print()

print()

# Tutorial
for x in range(n):
	print((str(x+1)+' ')*n)

#4. print alphabate square with n number of rows.
# A = 65 , B = 66 , C = 67 , D = 68 ....

print()

for x in range(n):
	print((chr(65+x)+' ')*n)

#5. Print right angle triangle pattern with * symbol.

print()

# Mine
for x in range(n):
	print('* '*(x+1))

print()

# Tutorial
for x in range(n):
	for j in range(x+1):
		print('*',end=' ')
	print()

#6. Print inverted right angle triangle pattern with * symbol.

print()

# Mine
for x in range(n):
	for j in range(n-x-1):
		print(' ',end=' ')
	print('* '*(x+1))

print()

for x in range(n):
	print('* '*(n-x))

print()

#7. Pyramid pattern with * symbol.
# 1111*1
# 111*1*1
# 11*1*1*1
# 1*1*1*1*1
# *1*1*1*1*1

# Mine
for x in range(n):
	for j in range(n-x-1):
		print(' ',end='')
	print('* '*(x+1))

print()

# Tutorial
for x in range(n):
	print(' '*(n-x-1)+'* '*(x+1))

#8. Inverted Pyramid pattern with * symbol.

# *1*1*1*1*1
# 1*1*1*1*1
# 11*1*1*1
# 111*1*1
# 1111*1

print()

# Mine
for x in range(n):
	print(' '*x+'* '*(n-x))

print()

#9. Diamond pattern with * symbol.

# Mine

for x in range(n):
	print(' '*(n-x-1)+'* '*(x+1))
for	x in range(n):
	print(' '*(x+1)+'* '*(n-x-1))