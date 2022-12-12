# ~a => Urnary operator
# a + b => Binary operator

# Ternary Operator
a = 10
b = 20
c = 30 if a>b else 40
print(c)

print('-------------------------------')
a = int(input('Enter 1st Number :- '))
b = int(input('Enter 2nd Number :- '))

min = a if a<b else b
print('The Min Value :- ',min)
print('-------------------------------')

# Nesting of Ternary operators
print('-------------------------------')
a = int(input('Enter 1st Number :- '))
b = int(input('Enter 2nd Number :- '))
c = int(input('Enter 3rd Number :- '))

min = a if a<b and a<c else b if b<c else c
print('The Min Value :- ',min)
print('-------------------------------')

a = int(input('Enter 1st Number :- '))
b = int(input('Enter 2nd Number :- '))
c = int(input('Enter 3rd Number :- '))

max = a if a>b and a>c else b if b>c else c
print('The Max Value :- ',max)
print('-------------------------------')

a = int(input('Enter 1st Number :- '))
b = int(input('Enter 2nd Number :- '))

ans = f'{a} is equal to {b}.' if a==b else f'{a} is greater than {b}.'  if a>b else f'{a} is smaller than {b}.'
print(ans)





