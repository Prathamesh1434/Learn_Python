# extend() => To add all elements of given sequence to the list.

order1 = ['Chicken','Mutton','Fish']
order2 = ['KF','KO','RC']
order1.extend(order2)

print("Adding order2 element to order1 => ",order1)

print()

l1  = [10,20,30]
l2 = [40,50]
l1.append(l2)
print('length l1 => ',len(l1))
print("l1 after append() method => ",l1) #  [10, 20, 30, [40, 50]]

l1  = [10,20,30]
l2 = [40,50]
l1.extend(l2)
print('length l1 => ',len(l1))
print("l1 after extend() method => ",l1) # [10, 20, 30, 40, 50]

print()

l1  = [10,20,30]
l1.append('ABC')
print('length l1 => ',len(l1))
print("l1 after append() method => ",l1) # [10, 20, 30, 'ABC']

l1  = [10,20,30]
l1.extend('ABC')
print('length l1 => ',len(l1))
print("l1 after extend() method => ",l1) # [10, 20, 30, 'A', 'B', 'C']