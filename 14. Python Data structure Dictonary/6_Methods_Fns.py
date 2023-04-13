# len()
d1 = {100:'A',200:'B',300:'C'}
print('length of d1 =>',len(d1))

# get()
print('d1 => ',d1)
print('Value for key 300 =>',d1.get(300))
print('Value for key 700 =>',d1.get(700))
print('Value for key 700 =>',d1.get(700,'Z')) # 'Z' is default value.
print()

# update()
print('d1 => ',d1)
d2 = {400:'X',500:'Y',300:'P'}
print('d2 => ',d2)
d1.update(d2)
print('d1 after update => ',d1)