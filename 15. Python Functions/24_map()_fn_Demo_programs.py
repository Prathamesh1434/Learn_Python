# filter() 
# input_element : 10 elements
# output_element : <=10 elements

# map()
# input_element : 10 elements
# output_element : 10 elements

# map(function,sequence)
l = [1,2,3,4,5]
def sqIt(n):
	return n*n

l1 = list(map(sqIt,l)) # returns <map object at 0x100faf79> => cast map object to list.
print('Squres =>',l1)

l2 = list(map(lambda n:n*n,l))
print('Squres =>',l2)

l1 = [1,2,3,4,5]
l2 = [5,10,15,20,25]

indexWiseAdd = list(map(lambda x,y:x+y,l1,l2))
print('Index wise Addition =>',indexWiseAdd)

indexWiseMul = list(map(lambda x,y:x*y,l1,l2))
print('Index wise Multiplication =>',indexWiseMul)

l1 = [1,2,3,4,5,6] # len(l1) = 6
l2 = [5,10,15,20,25,30,40] # len(l2) = 7 => The last element will get ignore.

indexWiseAdd = list(map(lambda x,y:x+y,l1,l2))
print('Index wise Addition =>',indexWiseAdd)

l1 = [1,2,3,4,5]
l2 = [5,10,15,20,25]
l3 = [2,2,2,2,2]
indexWiseAdd = list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print('Index wise Addition =>',indexWiseAdd)