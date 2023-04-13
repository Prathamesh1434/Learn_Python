# 1 filter()

# filter(function,sequence)
# Without fiter fn
l = [0,1,2,3,4,5,6,7,8,9,10]
def isEven(n):
	if n%2==0:
		return True
	else:
		return False

l1 = []
for n in l:
	if isEven(n) == True:
		l1.append(n)

print('Even Numbers =>',l1)

# With filter function
l = [0,1,2,3,4,5,6,7,8,9,10]
l1 = list(filter(isEven,l)) # returns <filter object at 0x10052bfa0> => cast filter object to list.
print('Even Numbers =>',l1)

# filter With lambda function
l2 = list(filter(lambda n: n%2==0,l))
print('Even Numbers =>',l2)