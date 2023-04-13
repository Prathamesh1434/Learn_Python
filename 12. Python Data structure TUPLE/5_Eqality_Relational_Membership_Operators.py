# Equality Operator (== , !=)
t1 = ('Cat','Rat','Dog')
print('t1 => ',t1)
t2 = ('Cat','Rat','Dog')
print('t2 => ',t2)
t3 = ('CAT','RAT','DOG')
print('t3 => ',t3)
t4 = ('Rat','Dog','Cat')
print('t4 => ',t4)
print()
print('t1 == t2 => ',t1 == t2)
print('t1 == t3 => ',t1 == t3)
print('t1 == t4 => ',t1 == t4)

print()

# Relational Operators (< , <= , > , >=)
t1 = (10,20,30)
t2 = (30,15,40)

print('t1 < t2 => ', t1 < t2)
print('t1 > t2 => ', t1 > t2)

t1 = (10,20,30)
t2 = (10,5,70)

print('t1 < t2 => ', t1 < t2)
print('t1 > t2 => ', t1 > t2)

t1 = (10,20,30)
t2 = (10,20,30,40,50)

print('t1 < t2 => ', t1 < t2)
print('t1 > t2 => ', t1 > t2)
print()

# Membership operators:
t1 = (10,20,30)
print('10 in t => ',10 in t1)
print('60 not in t => ',60 not in t1)