def sum_sub(a,b):
    sum = a+b
    sub = a-b
    return sum,sub

x,y = sum_sub(eval(input('Enter the 1st number => ')),eval(input('Enter the 2nd number => ')))
print('The Sum => ',x)
print('The difference => ',y)

def calci(a,b):
    sum = a+b
    sub = a-b  
    mul = a*b
    div = a/b
    return sum,sub,mul,div # it will return sinlge tuple which will contain all the values.

cal = calci(20,10)
print('Type of return value of fn calci => ',type(cal))
print('cal => ',cal)
w,x,y,z = cal
print('The results are => ',w,x,y,z)