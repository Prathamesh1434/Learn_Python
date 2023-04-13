# Module naming conflicts
from module1 import *
add(10,20)
from module2 import *
add(10,20) # function will be considered from latest import.

import module1
import module2
module1.add(10,20)
module2.add(10,20)

from module1 import add as a1
from module2 import add as a2

a1(10,20)
a2(10,20)

def product(a,b):
	print('The product =>',a*b)