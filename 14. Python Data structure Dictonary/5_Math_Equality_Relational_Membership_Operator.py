# Operators
d1 = {100:'A',200:'B'}
print('d1 => ',d1)
d2 = {300:'c',400:'D'}
print('d2 => ',d2)
# d3 = d1 + d2 => TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# d4 = d1 * 3 => TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# Equality operator
print('d1 == d2 => ',d1 == d2)
d3 = {100:'A',200:'B'}
print('d3 => ',d3)
print('d1 == d3 => ',d1 == d3)

# relational (> , < , <= , >=) => Not applicable for dict.

# Membership operator => only for keys
print('100 in d1 => ',100 in d1)
print('100 not in d1 => ',100 not in d1)