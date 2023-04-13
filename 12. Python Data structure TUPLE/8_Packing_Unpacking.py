# Tuple Packing and unpacking
a = 10
b = 20
c = 30
d = 40

t = a,b,c,d # a,b,c,d packed in tuple t
print('t => ',t)

print()

t = (30,40,50,60)
a,b,c,d = t # t unpacked and assigned value to a,b,c,d
print('a =',a)
print('b =',b)
print('c =',c)
print('d =',d)
print()

# a,b,c = t => gives error => number of values and number of varaibles should be match.
# a,b,c,d,e = t => gives error => number of values and number of varaibles should be match.

a,*b = t # Type of b is list.
print('a =',a)
print('b =',b)