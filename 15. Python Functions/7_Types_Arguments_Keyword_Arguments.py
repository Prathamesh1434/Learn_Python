# 1 Keyword arguments => Most commonly used in python.
def sub(a,b):
    print('Sub => ',a-b)

sub(200,100) # a = 200 , b = 100 => Order is important.
sub(a = 200,b = 100) # a = 200 , b = 100 => Order is not important.
sub(b = 100,a = 200) # a = 200 , b = 100 => Order is not important.
# sub(a = 200,100) => SyntaxError: positional argument follows keyword argument÷
sub(200,b = 100) # 1st positional argument and followed by keyword argument is valid.