s1 ={10,20,30}
print('id of s1 => ',id(s1))
print('s1 =>',s1)
s2 = s1 # both variable will point out to same object => so if we change one of them , then object will get change.
print('id of s2 => ',id(s2))
print('s2 =>',s2)
s3 = s1.copy()
print('id of s3 => ',id(s3))
print('s3 =>',s3)
print()

s2 = s1
s1.pop()
print('s1 =>',s1)
print('s2 =>',s2)

# Set comprehension
s = {x*x for x in range(1,6)}
print('s =>',s)
print()

s = {2**x for x in range(1,6)}
print('s =>',s)
print()