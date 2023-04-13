# Write a program to generate 6-digit random number , which can be used as OTP
from random import *
for i in range(10):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

otp = ''
for i in range(6):
    otp = otp + str(randint(0,9))

print('OTP =>',otp)

# Write a program to generate a random password of 6 length where 1,3,5 characters are alphabate symbol 
# and 2,4,6 characters are digits.
alphabates = 'ABCEDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
print('Random PW => ',choice(alphabates),randint(0,9),choice(alphabates),randint(0,9),choice(alphabates),randint(0,9),sep='')
print('Random PW => ',choice(alphabates),choice(digits),choice(alphabates),choice(digits),choice(alphabates),choice(digits),sep='')

for i in range(10):
    print('Random PW => ',choice(alphabates),choice(digits),choice(alphabates),choice(digits),choice(alphabates),choice(digits),sep='')