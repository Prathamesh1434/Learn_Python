# Differences between List and tuples.
import collections
l = [10,20,30,40] # will take more memory => Performance is low => It is not hashable
t = (10,20,30,40) # will take less memory => Performance is high => It is hashable => We can add it to set and dict.

# print('Is the list hashable ? => ',isinstance(l,collections.Hashable)) # False
# print('Is the tuple hashable ? => ',isinstance(t,collections.Hashable)) # True
print('Hashcode of t => ',hash(t))
# print('Hashcode of l => ',hash(l)) => will give error as hascode is not availble for l.

s = {10,20,30,40,80} # Data will save on hashcode => Search is easy.
s.add(55)

# Dict => Based on hasocode and keys.
print()

s = {10,20}
print('s before adding t => ',s)
l = [10,20,30]
t = (10,20,30)
s.add(t)
print('s after adding t => ',s)

# s.add(l) => TypeError: unhashable type: 'list'
print()

d = {}
l = [10,20,30]
t = (10,20,30)
d[t] = 'A'
print('Dictonary d => ',d)

# d[l] = 'A' => TypeError: unhashable type: 'list'