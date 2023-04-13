# Collection related data type.
# Duplicates are allowed and insertion order is preserved.
# Hetrogenious objects are allowed.
# Dynamic
# We can change the context.
# List is mutable.
# representation => [elements]

l = []
l.append(10)
l.append('durga')
l.append(10)

print("List l => ",l)

l[0] = 77
print("List l after modification => "l)