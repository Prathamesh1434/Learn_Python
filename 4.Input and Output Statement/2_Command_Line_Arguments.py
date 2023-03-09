# EX => py test.py 10 20 30 

# Module => sys => variable => argv => list type variable

from sys import argv

print("Type of variable 'argv' :- ",type(argv)) 

# it will take arguments from the file name and index will move forward.

print('argv as list :- ',argv)


# Program to print command line arguments information
print('The no of cmd line arguments :- ',len(argv))
print('The list of cmd line arguments :- ',argv)

for x in argv : 
	print('value :- ',x)

# Program to print sum of given numbers provided as cmd line arguments.

args = argv[1:]

sum = 0
for y in args:
	sum = sum + int(y) # we need to cast as all the element to int as whatever we pass , it will be consider as string.

print('The Sum :- ',sum)







