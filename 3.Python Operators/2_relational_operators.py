# 1. Int Type
a = 10
b = 20

print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

# 2. String Type
a = 'a' # Unicode value = 97
print('Unicode of a :- ',ord(a))

b = 'b' # Unicode value = 98
print('Unicode of b :- ',ord(b))

s1 = 'Prathmesh'
s2 = 'Dnyanesh'

print(s1 < s2)
print(s1 <= s2)
print(s1 > s2)
print(s1 >= s2)

s1 = 'Prathmesh'
s2 = 'Prathmesh'

print(s1 < s2)
print(s1 <= s2)
print(s1 > s2)
print(s1 >= s2)

s1 = 'Prathmesh'
s2 = 'prathmesh'

print(s1 < s2)
print(s1 <= s2)
print(s1 > s2)
print(s1 >= s2)

# Boolean Type
print(True > False)
print(True >= False)
print(True < False)
print(True <= False)

# print(10 < 'Durga') => Error

a = 10
b = 20

if a > b:
	print('a is greater than b.')
else:
	print('a is not greater than b.')

# Chain for relational operators.
print(10 < 20)
print(10 < 20 < 30)
print(10 < 20 < 30 < 40)
print(10 < 20 < 30 < 40 > 50)