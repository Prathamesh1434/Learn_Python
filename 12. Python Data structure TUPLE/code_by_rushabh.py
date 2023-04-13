l = [1,2,3,4,5,6,8,9,10,12,15]

l1 = list(range(1,max(l)+1))
print(l1)

print('missing numbers => ')
for x in l1:
	if x not in l:
		print(x,end=' ')

print()