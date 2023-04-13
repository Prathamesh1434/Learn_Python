# Lambda function to find sum of given two numbers.
s = lambda a,b:a+b
print('The sum =>',s(200,300))
print('The sum =>',s(20,30))

# Lambda function to find biggest of given numbers.
# 2 input values.
bigger = lambda a,b:a if a>b else b
print('The greater number =>',bigger(200,300))
print('The greater number =>',bigger(-304,-400))

# 3 input values
bigger1 = lambda a,b,c:a if a>b and a>c else b if b>c else c
print('The greater number =>',bigger1(200,300,600))
print('The greater number =>',bigger1(-304,-400,111))