# 1. Mathematical functions from math module
import dmath
dmath.add(10,20)

dmath.mul(5,6)

# 2. import a module.
from math1 import * # => Import all modules.
x = f1()

from math2 import * # => Import all modules. 
# if math1 and math2 have same function , then python will give preference to the most recent module's function.
x = f1()

# Important functions present in maths:
print('----------------------------------------')
from math import *

r = int(input('Enter redius of the circle :- '))
print('Area of circle = ',pi * r ** 2)
print('Area of circle = ',pi * pow(r,2))

print(sin(pi/2))
print('----------------------------------------')

import math

print(dir(math))
print('Square root :- ',math.sqrt(16))

print('Value of pi :- ',math.pi)
print('Value of e :- ',math.e)

# create alias for module.
import math as m
print('Square root :- ',m.sqrt(16))

print('Value of pi :- ',m.pi)
print('Value of e :- ',m.e)

# print(math.floor(3.9)) => Throws error => Once you have created alias , we must have to use that only.

from math import sqrt
print(sqrt(16))

from math import sqrt as s,pi as p
print(s(16))
print(p)
