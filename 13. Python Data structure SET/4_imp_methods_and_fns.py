# len()
s = {10,20,30,40}
print('set s =>',s)
print('Length of s => ',len(s))

# add()
s.add(50)
print('set s =>',s)
print()

# update() => To add multiple items to the set.
s1 = {1,2,3}
print('set s1 =>',s1)
l = [4,5,6]
print('List l =>',l)
s.update(s1,l)
print('set s =>',s)
s.update(range(1,6),'Durga')
print('set s =>',s)