# setdefault(k,v) => if key is not availabe then only add the new item.
# d[key] = value => if key is not availabe then add the new item. => If its available , then update the corresponding value
d = {100:'A',200:'B',300:'C',400:'A'}
print('d =>',d)
d.setdefault(500,'X')
d.setdefault(400,'M')
print('d after using setdefault=>',d)
print()

# Aliasing & cloaning
d1 = {100:'A',200:'B',300:'C',400:'A'}
d2 = d1 # d1 and d2 pointing to the same reference => if we update d1 or d2 => both will get updated.
print('d1 =>',d1)
print('d2 =>',d2)
print('ID of d1 => ',id(d1))
print('ID of d2 => ',id(d2))
d3 = d1.copy() # Cloaning
print('d3 =>',d3)
print('ID of d3 => ',id(d3))