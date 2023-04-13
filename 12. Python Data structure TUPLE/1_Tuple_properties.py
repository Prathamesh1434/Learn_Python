# Tuple
# Order is appliable
# Duplicates are allowed
# Heterogeneous objects are allowed
# indexing & slicing allowed
# * Immutable 
# * (Elements) 

t = (10,'Durga',20,10)
t1 = 10,'Durga',20,10

print('Type of t => ',type(t))
print('Type of t1 => ',type(t1))

print()

print('Element at index 0 => ',t[0])
print('Element at index -1 => ',t[-1])


print()

l = [10,20,30,40]
l[0] = 777

print('List l => ',l)

k  = (10,20,30,40)
# t[0] = 777 => This will give TypeError: 'tuple' object does not support item assignment.