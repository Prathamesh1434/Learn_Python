# Random module
from random import *

# 1 random() => Generate random float number between 0 and 1 (0 < x < 1) => no argument function
print('Random number between 0 to 1 =>',random())
for i in range(10):
	print('Random number between 0 to 1 =>',random())
print()

# 2 uniform(begin,end) => begin < random float value < end
print('Random float value between (5,10) =>',uniform(5,10))
for i in range(10):
	print('Random float value between (5,10) =>',uniform(5,10))
print()

# 3 randint(begin,end) => begin < random integer value < end
print('Random integer value between (1,10) =>',randint(1,10))
for i in range(10):
	print('Random integer value between (1,10) =>',randint(1,10))
print()

# 4 randrange(begin,end,step) => range from begin to (end-1) 
# begin is optional(default is zero).
# step is optional(default is one).
# End is mendatory.
print('random value in range(0,5) => ',randrange(5)) # 0 to 4 => [0,1,2,3,4] => one value will get picekd from it.
print('random value in range(1,11) => ',randrange(1,11)) 
print('random value in range(1,30,3) with step 3 => ',randrange(1,30,3)) 
print('random value in range(0,101,10) with step 10 => ',randrange(0,101,10)) 
print()

# 5 choice() => To generate a random object from list , tuple , string , etc.
# The sequence should in indexable => applicable for List , Tuple , Set
fruits = ['Apple','Banana','Orange','Mango']
print('Fruit of choice =>',choice(fruits))
for i in range(5):
	print('Fruit of choice =>',choice(fruits))

alphabates = 'ABCEDEFGHIJKLMNOPQRSTUVWXYZ'
print('Random alphabate => ',choice(alphabates))
for i in range(5):
	print('Fruit of choice =>',choice(fruits))