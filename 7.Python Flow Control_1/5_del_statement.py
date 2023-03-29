# del => delete

x = 10 # x => 10
print('Before Deletion => ',x)

del x # => x is elegible for garbage colletion.

# print('after Deletion => ',x) => will give name error. => NameError: name 'x' is not defined

s1 = 'Prathmesh'
s2 = s1
s3 = s2

# s1 , s2 , s3=> refer to same object => if we use 'del s1' => s2 and s3 will still refer to same obj.

del s1,s2

print(s3)

# del vs immutable object.

s = 'Prathmesh' # stirng object is immutable.
# del s[0] => This is not possible => del s[0] => This is not possible.

# del vs None
x = 10
# in both cases object is elegibe for garbage collection.
del x  # => x variable deleted.
x = None # => now x pointing to None.
print(x)