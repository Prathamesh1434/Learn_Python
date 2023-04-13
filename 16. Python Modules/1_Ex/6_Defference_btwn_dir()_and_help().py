# 1 dir() => To list out all members of current modules.
# 2 dir(<Module_Name>) => To list out all members of specified modules.

x = 888
y = 999
def add(a,b):
	print(a+b)

print('All members inside current module =>',dir())

import math
print('All members inside math module =>',dir(math))

# Diff between dir() and help() function
# dir(math) => All member of math module.
# help(math) => Gives all info about functions
print('Info abt all members of math module =>',help(math))