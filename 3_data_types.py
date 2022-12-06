# 1. Int Data Type

a = 10
print('Type of a :- ',type(a))

# Binary to Decimal
a = 0B1111
b = 0b1111

print('value of a :- ',a)
print('value of b :- ',b)

# Octal to Decimal

a = 0O234
b = 0o234

print('value of a :- ',a)
print('value of b :- ',b)

# Hexa Decimal to Decimal

a = 0XFACE
b = 0xBeef

print('value of a :- ',a)
print('value of b :- ',b)

# Base Conversion

print(bin(15))
print(bin(0o234))
print(bin(0xFace))

print(oct(10))
print(oct(0b1111))
print(oct(0xFace))

print(hex(100))
print(hex(0b1111))
print(hex(0o2345))

# 2. Float Data Type

f = 1.234
print('Type of f :- ',f)

f = 1.2e3 # e3 => 10 power 3 in multiplication

# 3. Complex Data Type

a = 1.5 + 10j
print('type of a :- ',a)
print('Real part of a :- ',a.real)
print('Img part of a :- ',a.imag)

a = 0B11 + 5.5j # Real part as bin , oct and hex is allowed , But img part should be in decmial
print('Ex of Complex No :- ',a)

# 4. Bool Data Type

a = 10
b = 20
c = a<b
print('Result of a < b :- ',c)

print(True + True)
print(True - False)

# 5. str Data Type

s1 = "Prathmesh"
s2 = 'Dnyanesh'

print(s1)
print(s2)

s3 = """Prathmesh
Gayakwad"""    # For multiline output , we need to use tripple coat.
print(s3)

s4 = '''Dnyanesh
Gaykwad'''
print(s4)

s5 = ''' We can include " , ' char in single tripple coat.'''
s6 = """We can include " , ' char in double tripple coat."""
s7 = 'We can include " in single coat.'
s8 = "We can include ' in double coat."

print(s5)
print(s6)
print(s7)
print(s8)

# Slicing of Strings

s = "Prathmesh"
print('Index 0 letter : - ',s[0]) # => This index starts from left to right.
print('Index -1 letter : - ',s[-1]) # => This index starts from right to left.

print('String from index 1 to 4 :- ',s[1:4])
print('String from index 1 to last :- ',s[1:])
print('String from index 0 to 4 :- ',s[:4])
print('String from index first to last :- ',s[:])
print('Print String 3 times :- ',s*3)
print('lenght of string s :- ',len(s))


















