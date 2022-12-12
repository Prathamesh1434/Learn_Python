# 1. '='
x = 10
print('Value of x = ',x)

# 2. Compound assignment operator.

x = 10
x += 20 # x = x+ 20 = 10 + 20
print('Value of x = ',x)

x = 10
x &= 5 # x = x & 5
print('Value of x = ',x)

x = 10
x **= 2 # x = x ** 2
print('Value of x = ',x)

x = 10
# x++ => Gives Error

x = 10
# x-- => Gives Error

x = 10
print(++x) # +(+(x))
print(++++x) # (+(+(+(+(x)))))

print(-x) # -(x)
print(--x) # -(-(x))

