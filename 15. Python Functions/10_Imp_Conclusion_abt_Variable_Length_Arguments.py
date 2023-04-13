def f1(x,*y):
	print('x =>',x)
	for y1 in y:
		print('Element of y =>',y1)

f1(10,20,30,40) # x = 10 , y = (20,30,40)
f1(10) # x = 10 , y = ()
# f1() => TypeError: f1() missing 1 required positional argument: 'x'
print()

def f2(*x,y):
	print('Tuple x =>',x)
	print('y =>',y)

f2(10,20,30,40) # f2() missing 1 required keyword-only argument: 'y'
f2(10,20,30,y=40)

# def f3(*x,*y): => We can't take more than one variable length argument
# 	print('Tuple x =>',x)
# 	print('Typle y =>',y)