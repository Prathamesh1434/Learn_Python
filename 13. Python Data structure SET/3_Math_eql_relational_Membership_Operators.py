s1 = {10,20,30}
s2 = {30,10,20}

# s3 = s1 + s2 => TypeError: unsupported operand type(s) for +: 'set' and 'set'
# s3 = s1 * s2 => TypeError: unsupported operand type(s) for *: 'set' and 'set'

print('s1 = s2 => ',s1==s2)
print('s1 != s2 => ',s1!=s2)
print()

# Relational operator => Not meaningful
s1 = {10,20,30}
s2 = {20,10,5,6,7}
print('s1 < s2 => ',s1 < s2)
print('s1 <= s2 => ',s1 <= s2)
print('s1 > s2 => ',s1 > s2)
print('s1 >= s2 => ',s1 >= s2)
print()

# Membership operators
s = {10,20,30,40}
print('10 in s => ',10 in s)
print('10 not in s => ',10 not in s)