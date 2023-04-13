# filter() 
# input_element : 10 elements
# output_element : <= 10 elements

# map()
# input_element : 10 elements
# output_element : 10 elements

# reduce()
# input_element : 10 elements
# output_element : 1 element

# reduce(fuction,sequence)
l = [10,20,30,40,50]

from functools import reduce

result = reduce(lambda x,y:x+y,l) # need to import it explicitly.
print('Addition =>',result)

# Find the sum of first 100 Numbers by using reduce() fn.
add1to100 = reduce(lambda x,y:x+y,range(1,101))
print('Addition from 1 to 100 =>',add1to100)