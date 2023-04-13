# Sorting elements of list
# numbers => Ascending order
# String => Alphabatic order

# sort() => List specific 
l = [10,5,15,0,10]
print('List before sort => ',l)
l.sort() # or l.sort(reverse = False)
print('List after sort => ',l)

print()

l = ['Banana','Cat','Apple']
print('List before sort => ',l)
l.sort() # or l.sort(reverse = False)
print('List after sort => ',l)

print()

l = [10,5,15,0,10]
print('List before sort => ',l)
l.sort(reverse = True)
print('List after sort => ',l)

print()

l = ['Banana','Cat','Apple']
print('List before sort => ',l)
l.sort(reverse = True)
print('List after sort => ',l)

l = [40,20,'B','A']
# l.sort() => will give error => elements of list should be of homogeneous type.

print()

# sorted() => Python inbult function
l = [10,5,15,0,10]
print('List before sorted => ',l)
l2 = sorted(l)
print('List after sorted => ',l2)