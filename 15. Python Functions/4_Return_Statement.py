# Return Statement
# Write a functrion to accept 2 numbers as input and returns sum.
def addition(a,b):
    sum = a+b
    return sum

result = addition(eval(input('Enter the value of a => ')),eval(input('Enter the value of b => ')))

print('Addition =>',result)

print('The Sum => ',addition(eval(input('Enter the value of a => ')),eval(input('Enter the value of b => '))))

def f1(): # NO return value => Default return value is none.
    print('Hello !')

x = f1()
print('The return value => ',x)

# Write a function to find factorial of given positive int value.
def factorial(a):
    f = 1
    if a>=0:
        for i in range(a+1):
            if i>0:
                f = f*(i)
    return f

a = eval(input('Enter the number to get factorial => '))
b = factorial(a)

print('The factorial of {} = {}'.format(a,b))

def fact(num):
    result =1
    while num >=1:
        result = num * result
        num = num -1
    return result

a = eval(input('Enter the number to get factorial => '))
b = fact(a)
print('The factorial of {} = {}'.format(a,b))
for i in range(1,6):
    print('The fact of',i,'=>',fact(i))