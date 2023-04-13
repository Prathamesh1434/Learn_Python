# List Comprehension
l = [1,2,3,4,5,6,7,8,9,10]

# Normal Way
l = []
for i in range(1,11):
	l.append(i)

print('l => ',l)

print()

# Comprehension concept
l = []
l = [x for x in range(1,11)]
print('l => ',l)

print()
l = []
l = [x for x in range(1,21) if x%4==0]
print('l => ',l)

print()

# Creation of List value with Square values from 1 to 10. => l = [1,4,9,16,25,36,49,64,81,100]
l = [x*x for x in range(1,11)]
print('l => ',l)

print()

# required op => l = [2,4,8,16,32]
l = [2**x for x in range(1,6)]
print('l => ',l)

print()

# l = [10,20,30,40,50,60,70,80,90,100]
l = [x for x in range(1,101) if x%10==0]
print('l => ',l)

print()

# Create a list with elements present in l1 but not in l2. => l3 = [10,20]
l1 = [10,20,30,40]
l2 = [30,40,50,60]

l3 = [x for x in l1 if x not in l2]
print('l3 => ',l3)
print()

# Create List with present in both l1 and l2
l4 = [x for x in l1 if x in l2]
print('l4 => ',l4)

print()

l  = ['Balaian','Nag','Venki','Chini']
l1 = [x[0] for x in l]
print('l1 => ',l1)
print()

s = 'the quick brown fox jumps over the lazy dog'
words = s.split()
print('words => ',words)

l1 = [[x.upper(),len(x)] for x in words]
print('l1 => ',l1)
print()