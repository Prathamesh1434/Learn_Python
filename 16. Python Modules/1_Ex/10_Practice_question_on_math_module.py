# You are creating a function that manipulates a number.the function has the following requirements:
# A floor value passed to the function.
# The function must take absolute value of the float.
# Any decimal point after the integer must be removed.
# which two math fucntions should be used ?

# math.frexp(x) => 
# math.floor(x) => 12.30 => 12
# math.fabs(x) => -12.30 => 12.30 => Ignore the sign of value.
# math.fmod(x) => 
# math.ceil(x) => 
from math import *
print(fabs(-12.30))
print(floor(fabs(-12.30)))