# 1. + , - , * , %
a = 10
b = 3
c = 10.0
print('addition = ' ,a + b)
print('Substraction = ',a - b)
print('Multiplication = ',a * b)
print('Remainder = ',a % b)

# 2. / => Normal division Operator | 6. // => Floor division Operator
print('Normal Division :- ',a/b) # Normal division always gives floating point result.
print('Floor Division :- ',a//b) # gives ans in Int as both arguments are in int.
print('Floor Division :- ',c//b) # gives ans in Float as one argument is in float.

# 3. ** => Exponential Operator / Power Operator
print('a power b :- ',a**b)

# 3. Use of + operator for different uses
a = 'Prathmesh'
b = 'Gayakwad'
c = 10

print(a + b)
# print(b+c) => IN python , We can't string and Int directly.
print(a + str(c)) # =>  Use type casting.

# 4. Use of * operator
a = 'Prathmesh'
b = 'Gayakwad'

print(a * 3) # => Repeats value of a 3 times.
print(3 * a) # => Repeats value of a 3 times.
# print(a * b) => Multiplication of str values is not allowed.

#print(a * '3') => Multiplication of str values is not allowed.
print(a * int('3')) # => Allowed by using typeCasting.

# 5. Use of / or // for dividor zero.
# print(10/0) => gives ZeroDivisionError.
# print(10.0//0) => gives ZeroDivisionError.
# print(10/0) => gives ZeroDivisionError.

print('Prathmesh' * True)
print('Prathmesh' * False)