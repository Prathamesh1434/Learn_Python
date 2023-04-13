# pop(key) => it removes the item associated with corresponding key. => if key is not available => ValueError
d1 = {100:'A',200:'B',300:'C',400:'A'}
print('d1 => ',d1)
print('Value associated with the removed key =>',d1.pop(300))
print('d1 after pop => ',d1)
# d1.pop(700) => ValueError
print()

# pop(key,value)
d1 = {100:'A',200:'B',300:'C',400:'A',500:'C'}
print('d1 => ',d1)
print('Value associated with the removed key =>',d1.pop(700,'Key is not in Dict.'))
print('d1 after pop => ',d1)
print()

# popitem() => Removes random item.
# pop(key,value)
d1 = {100:'A',200:'B',300:'C',400:'A',500:'C'}
print('d1 => ',d1)
print('Item removed => ',d1.popitem()) # if dict is empty and we use this method => it will give KeyError.
print('d1 after popitem => ',d1)
print()

# clear()
d1 = {100:'A',200:'B',300:'C',400:'A',500:'C'}
print('d1 => ',d1)
print('Clear dict => ',d1.clear())
print('d1 after clear => ',d1)
print()