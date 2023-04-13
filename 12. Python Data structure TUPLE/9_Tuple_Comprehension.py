l = [x for x in range(1,6)]
print('Type of l => ',type(l))
print('l = ',l)
print()
 
t = (x*x for x in range(1,6)) # Comprehension object is not applicable for tuple.
print('Type of t => ',type(t)) # <class 'generator'>
print('t = ',t) # <generator object <genexpr> at 0x104df5d90>