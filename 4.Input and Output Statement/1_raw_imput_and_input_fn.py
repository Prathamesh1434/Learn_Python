# raw_input() and input()

# Avaliable in Python 2.x
# x = raw_input('Enter Some Value :- ') # it always of string type.
# print('Type of x :- ',type(x))
# y = int(x)
#
# Avaliable in Python 3.x
x = input('Enter Some Value :- ') # This fun behaviour is same as Python 2.x raw_input fn.
print('Type of x :- ',type(x)) # => Always str type for any value.

print('----------------------------------')
x = input('Enter 1st Number :- ')
y = input('Enter 2nd Number :- ')
i = int(x)
j = int(y)
print('Sum = ',i+j)
print('----------------------------------')
x = int(input('Enter 1st Number :- '))
y = int(input('Enter 2nd Number :- '))
print('Sum = ',x+y)
print('----------------------------------')
print('The Sum = ',int(input('Enter 1st Number :- ')) + int(input('Enter 2nd Number :- ')))
print('----------------------------------')

eno = int(input('Enter Employee Number :- '))
ename = input('Enter Employee Name :- ')
esal = float(input('Enter Employee Salary :- '))
eaddr = input('Enter Employee City :- ')
married = bool(input('Employee Married ? [True/False] :- ')) # => any string => True , Empty String => False
married1 = eval(input('Employee Married ? [True/False] :- ')) # => Consider ,| i/p(True) => True and i/p(False) => False | in bool data type.

print('Employee Number :- ',eno)
print('Employee Name :- ',ename)
print('Address :- ',eaddr)
print('Salary :- ',esal)
print('Married :- ',married)
print('Married1 :- ',married1)
print('----------------------------------')

# Read multiple values from keyboard

s = input('Enter 2 numbers: ') # Returns String type value. => 10 20
print(s)

l = s.split() # Returns List as default seprator for values is space. => ['10' , '20']
print('Values as List :- ',l)

l1 = [int(x) for x  in l] # Typecast each element to Int type. => [10 , 20]
print('values :- ',l1)

a,b = l1 # list unpacking concept => a = 10 , b = 20
print('a = ',a)
print('b = ',b)

print('The Sum :- ',a+b )

a,b = [int(x) for x in input('Enter 2 Numbers:- ').split()] # two numbers should have space between them.
print('The Sum :- ',a+b)

a,b = [int(x) for x in input('Enter 2 Numbers:- ').split(',')] # two numbers should have comma between them.
print('The Sum :- ',a+b)

print('----------------------------------')

# Read 3 values from the keyboard with comma sepration and print the sum.

a,b,c = [float(x) for x in input("Enter 3 numbers with comma sepration :- ").split(',')]
print('The Sum :- ',a+b+c)

print('----------------------------------')

# eval() function => it will determine the data type for the input provided and able to evaluate the mathematical expression.

x = eval(input('Enter Something :- '))
print('value of x :- ', x , ' | Type of x :- ', type(x))

print('----------------------------------')


















