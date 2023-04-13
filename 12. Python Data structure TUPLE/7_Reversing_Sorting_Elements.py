# Reversing elements of tuple
# reverse() method in not available in tuple as it is immutable.

t = (10,20,30,40)
print('t => ',t)

r = reversed(t)
t1 = tuple(r)
print('reversed t1 => ',t1)

# Sorting the elements of tuple.
# sort() method in not available in tuple as it is immutable.

t = (20,5,10,15,0)
print('t => ',t)
l = sorted(t)
t1 = tuple(l)
print('Ascending Sorted t1 => ',t1)

t = (20,5,10,15,0)
print('t => ',t)
l = sorted(t,reverse = True)
t1 = tuple(l)
print('Descending Sorted t1 => ',t1)
print()

# max and min functions for tuple
t = (20,10,0,5,15)
print('t => ',t)
print('max in t => ',max(t))
print('min in t => ',min(t))