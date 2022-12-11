# 1. List
l = [10,'Durga',20,10,30]
print('Type of l :- ',type(l))
print(l)

print('Element at index 0 :- ',l[0])
print('Element at index -1 :- ',l[-1])
print('Element from index 1 to 4 :- ',l[1:4])

l.append(40) # Add 40 to the list. And list is mutable.
l.append(20)
l.append(30)
l.append(60)
print(l)

l.remove(30) # Remove 30 from the list.
print(l)


# 2. Tuple => Exactly same as list , except it is immutable.
t = (10,20,30,10,20,'Durga')
print('Type of t :- ',type(t))
print(t)

print('Element at index 0 :- ',t[0])
print('Element at index -1 :- ',t[-1])
print('Element from index 1 to 4 :- ',t[1:4])

# t[0] = 7777 => TypeError => As tuple is immutable.
# t.append(90) => Attribute error => We can't add the element.
# t.remove(10) => Attribute error => We can't remove the element.

t = () # Empty tuple
print(t)
print('Type of t :- ',type(t))

t = (10) # => This represent Int Type.
print(t)
print('Type of t :- ',type(t))

t = (10,) # => This represent single value tuple
print(t)
print('Type of t :- ',type(t))

# 3. Set
s = {10,20,30,40}
print(s)
print('Type of s :- ',type(s))

s = {10,20,10,'Durga',30,40} # => while printing duplicate will be removed.
print(s)

# print('Element at index 0 :- ',s[0]) => Not possible
# print('Element at index -1 :- ',s[-1]) => Not possible
# print('Element from index 1 to 4 :- ',s[1:4]) => Not possible

s.add(50) # Special method for set.
print('Updated value of s => ',s)

s.remove(30)
print('Updated value of s => ',s)

s = {} # This is the empty dictonry.
print('Type of s :- ',type(s))

s = set()
print('Type of s :- ',type(s))

# 4. FrozenSet # => Immutable (Other properties are same as Set.)
s = {10,20,30,40}
fs = frozenset(s)
print(fs)

print('Type of fs :- ',type(fs))

# fs.add(50) => Attribute error => We can't add the element.
# fs.remove(30) => Attribute error => We can't reomve the element.

# 5. Dict => Key-Value pair
d  = {100:'Prathmesh' , 200:'Dnyanesh' , 300:'Tinku'}
print(d)

print('Type of d :- ',type(d))

d = {} # Empty dictonary
d[100] = 'Sandip'
d[200] = 'Nikhil'
print(d) # Order may vary.

d[100] = 'Shiva' # Duplicate keys are not allowed , but we won't get any error , Shiva will replace the old value.
print('Updated dict d :- ',d)

d[300] = 'Shiva' # Duplicate values are allowed.
print('Updated dict d :- ',d)

# print('Element at index 0 :- ',d[0]) => Not possible
# print('Element at index -1 :- ',d[-1]) => Not possible
# print('Element from index 1 to 4 :- ',d[1:4]) => Not possible

# 6. range
r = range(10) # 0 to 9
print(r)

print('Type of r :- ',type(r))

for x in r:
	print(x)

r = range(10,20) # 10 to 19
print(r)

for x in r:
	print(x)

r = range(2,21,2) # 10 to 39 => incremant by 2
print(r)

for x in r:
	print(x)

r = range(20,0,-2) # 10 to 39 => decrement by 2
print(r)

for x in r:
	print(x)

r = range(10,21) # 10 to 20
print(r)

print('Element at index 0 :- ',r[0])
print('Element at index -1 :- ',r[-1])

r1 = r[1:4]

print('Element from index 1 to 4 :- ')

for x in r1:
	print(x)

# r[1] = 1000 => Not allowd => range is immutable.

# 7. Bytes => Allowed values :- [0 to 255]
l = [10,20,30,40]
b = bytes(l)
print(b)

print('Type of b :- ',type(b))

for x in b:
	print(x)

print('Element at index 0 :- ',b[0])
print('Element at index -1 :- ',b[-1])

# b[0] = 77 => Not allowed , bytes is immutable. 

# 8. bytearray => Allowed values :- [0 to 255]
l = [10,20,30,40]

ba = bytearray(l)
print(ba)

print('Type of ba :- ',type(ba))

for x in ba:
	print(x)


print('Element at index 0 :- ',ba[0])
print('Element at index -1 :- ',ba[-1])

ba[0] = 77 # => allowed , bytearray is mutable.

print('Updated bytearray :- ')

for x in ba:
	print(x)
