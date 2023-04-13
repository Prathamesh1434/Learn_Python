# Concatination operator (+)
l1 = [10,20,30]
l2 = [40,50,60]
l3 = l1 + l2 # Both arguments should be of list type.

l2 = l1 + [40]

print('l1 => ',l1)
print('l2 => ',l2)
print('l3 => ',l3)

# l2 = l1 + (10,20,30) => list + tuple => not allowed.

print()

# Repetition operator(*)
l1 = [10,20]
l2 = l1 * 2 # one argument should be integer.
print('l2 => ',l2)

l1 = [10,20]
l2 = [30,40]
l3 = l1 + l2
l4 = l3 * 3

print('l4 => ',l4)