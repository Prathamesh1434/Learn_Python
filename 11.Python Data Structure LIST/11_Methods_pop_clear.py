# pop()
l = [10,20,30]
print('List before pop => ',l)
 # it will remove the last element.
print('popped element => ',l.pop())
print('List after pop => ', l)
print('popped element => ',l.pop())
print('List after pop => ', l)
print('popped element => ',l.pop())
print('List after pop => ', l)
# print('List after pop => ', l.pop()) => This will give index error as no element in the list.

print()

# pop(index)
l = [10,20,30,40]
print('List before pop => ',l)
print('popped element at index 1 => ',l.pop(1))
print('List after pop => ', l)
# print(l.pop(100)) => This will give index error.

print()

# clear()
l = [10,20,30,40]
print('List before clear => ',l)
print('List after clear => ',l.clear())