# Function parameters => acts as inputs to the function.
# Write a function ti take the name of the student as input and print wish message for him.
def wish(s_name):
    print('Hi {} , Welcome to the KITS !!!'.format(s_name))

wish(input('Enter the name of the student => ')) # Need to provide required parameter , otherwise we will get error.

# Write a function to take number as input and print its square value.
def square(a):
    print('Square of {} = {}'.format(a,a*a))

square(eval(input('Enter the number => ')))