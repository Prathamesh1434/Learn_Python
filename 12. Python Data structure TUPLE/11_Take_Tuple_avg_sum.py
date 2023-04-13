import math
# Take_Tuple_of_Numbers_from_the_keyboard_and_print_sum_average.py
t = eval(input('Enter tuple of numbers => '))
k = 0
for x in t:
	k += x

print('The Sum => ',k)
print('The average => ',k/len(t))

print('The Sum => ',sum(t)) # applicable for tuple , list , set
print('The average => ',avg(t)) # applicable for tuple , list , set