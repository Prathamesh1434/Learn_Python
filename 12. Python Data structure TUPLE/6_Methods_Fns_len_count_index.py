# len() => Returns num of elements in tuple.
t = (10,20,30,40)
print('legth of t => ',len(t))
print()

# count() => Numbers of occourances of specified elements in tuple
t = (1,1,2,4,5,3,3,5,3)
print('1 in t => ',t.count(1))
print('7 in t => ',t.count(7))
print()

# index() => returns 1st occourance of specified element.
t = (1,1,2,4,5,3,3,2,5,3)
print('1st occourance of 2 in t => ',t.index(2))
# print('1st occourance of 40 in t => ',t.index(40)) => This will give error as 40 is not in tuple t.