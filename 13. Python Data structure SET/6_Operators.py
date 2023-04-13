# union()
s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.union(s2)
print('s1 =>',s1)
print('s2 =>',s2)
print('s3 =>',s3)

s3 = s1|s2
print('s3 =>',s3)
print()

# intersection()
s4 = s1.intersection(s2)
s4 = s1&s2
print('s4 =>',s4)
print()

# difference()
s5 = s1.difference(s2)
s3 = s1-s2
print('s5 =>',s5)
print()

# symmetric_difference()
s6 = s1.symmetric_difference(s2)
s6 = s1^s2
print('s6 =>',s6)