# Empty Set
s = set()
print('Type of s =>',type(s)) # Type of s => <class 'set'>
print('set s =>',s)

# if we have data already.
s = {10,20,30,40}
print('set s =>',s)
print()

# By using set() function:
l = [10,20,30,40,10]
print('list l => ',l)
s = set(l)
print('set s =>',s)
print()

s = set(range(0,101,10))
print('set s =>',s)

s = set('apple')
print('set s =>',s)

s = eval(input('Enter set of values => '))
print('set s =>',s)