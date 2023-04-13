l1 = [10,20,30,40]
l2 = l1

print('l1 => ',l1)
print('id of l1 => ',id(l1))
print('l2 => ',l2)
print('id of l2 => ',id(l2))
# l1 and l2 are the reference varaible which will point to the same object.
l1[1] = 7777 # It will change l1 and l2 both.
print('l1 after change => ',l1)
print('l2 after change => ',l2)

print()

# Cloning : Process of creating duplicate object.
l1 = [10,20,30,40,50]
l2 = l1[::] # It will create new object
print('l1 => ',l1)
print('id of l1 => ',id(l1))
print('l2 => ',l2)
print('id of l2 => ',id(l2))

# l1 and l2 are the reference varaible which will point to the same object.
l1[1] = 7777 # It will not change l2.
print('l1 => ',l1)
print('l2 => ',l2)

l3 = l1.copy()
print('l3 => ',l3)