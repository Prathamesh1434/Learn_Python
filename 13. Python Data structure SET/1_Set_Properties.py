# Duplicates not allowed
# order is not imp
# indexing and slicing concept is not appicable.
# {elements}
# Heterogeneous objects are allowed
# Mutable
# Union , intersection etc are allowed
# {} => b y default its dict not set

s = {} # Type of s => <class 'dict'>
print('Type of s =>',type(s))

s = set()
print('Type of s =>',type(s)) # Type of s => <class 'set'>
print()

s.add(10)
s.add('z')
s.add('A')
s.add(20)
s.add(10)

print('set s =>',s)

# print(s[0]) => TypeError: Set object does not support indexing.