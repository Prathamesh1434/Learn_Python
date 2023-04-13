# Write a program to enter name and marks into a dictonary and display it on screen
n = int(input('Enter number of students => '))
d = {}
for i in range(n):
	name = input('Enter name of student => ')
	marks = eval(input('Enter marks of student =>' ))
	d[name] = marks

print('Students details => ',d)

print('*'*30)
print('Name','\t\t','Marks')
print('*'*30)
for name in d:
	print(name,'\t\t',d[name])