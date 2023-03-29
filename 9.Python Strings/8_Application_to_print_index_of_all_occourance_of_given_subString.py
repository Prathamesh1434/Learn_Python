s = 'ABCABCABCA'
i = s.find('ABC')
print(i)
i = s.find('ABC',3,len(s))
print(i)
i = s.find('ABC',6,len(s))
print(i)
i = s.find('ABC',9,len(s))

s = 'ABCABCABCA'
subS = input('Enter SubString to search => ')

i = s.find(subS)
if i == -1:
	print("Substring '{}' is not found.".format(subS))
while i != -1:
	print("'{}' present at index : {}".format(subS,i))
	i = s.find(subS,i+len(subS),len(s))