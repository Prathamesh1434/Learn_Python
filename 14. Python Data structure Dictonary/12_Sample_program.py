# Write program to take dictonary from keyboard
d = eval(input('Enter dictonary => '))
print('d =>',d)
s = 0
for item in d.items():
	s = s+item[1]
print('Sum of values =>',s)
print()
print('Sum of values =>',sum(d.values()))