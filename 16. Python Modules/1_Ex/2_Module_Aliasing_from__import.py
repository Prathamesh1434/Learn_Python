# Module Aliasing
import prathmesh_Math as m # we must need to use m to access any attribute from module 'prathmesh_Math'.
print('x =>',m.x)
print('y =>',m.y)

m.add(10,20)
m.product(10,20)
print()

# from...import:
from prathmesh_Math import * # we can access all attributes of module 'prathmesh_Math' without alias.
print('x =>',x)
print('y =>',y)

add(10,20)
product(10,20)