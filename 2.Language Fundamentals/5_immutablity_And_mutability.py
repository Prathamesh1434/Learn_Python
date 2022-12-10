# Immutablity
x = 10
print('value of :- ',x)
print('Id of x :- ',id(x)) # => Will create one object.

x = x + 1
print('value of :- ',x)
print('Id of x :- ',id(x)) # => Will create another object.

x = 10
y = x
print('value of x :- ',x)
print('value of y :- ',y)
print('Address of x :- ',id(x)) # => object is same , as value not changed.
print('Address of y :- ',id(y)) # => object is same , as value not changed.

y = y + 1
print('value of :- ',y)
print('Address of y :- ',id(y)) # => new object will get created.

# For 'int' datatype
a = 10
b = 10
c = 10

print('Address of a :- ',id(a))
print('Address of b :- ',id(b))
print('Address of c :- ',id(c))

print('is a and b are equal ? => ',a is b)

# For 'float' datatype
a = 1000.234
b = 1000.234
c = 1000.234

print('Address of a :- ',id(a))
print('Address of b :- ',id(b))
print('Address of c :- ',id(c))

print('is a and b are equal ? => ',a is b)

# For 'boolean' datatype
a = True
b = True

print('is a and b are equal ? => ',a is b)

# For 'string' datatype
a = 'Prathmesh'
b = 'Prathmesh'

print('is a and b are equal ? => ',a is b)

# For 'complex' datatype
l = 10+20j
m = 10+20j

print('is l and m are equal ? => ',id(l) is id(m)) # Exceptional case => will always create new object.

# Example of mutability 
# Ex 1
l = [10 ,20 ,30]
print("Values in list 'l' :- ",l)
print("Address of list 'l' :- ",id(l))

l[0] = 7777
print("Updated values in list 'l' :- ",l)
print("Address of list 'l' :- ",id(l))

# Ex 2
l1 = [10,20,30,40]
l2 = l1

print('List l1 :- ',l1)
print('List l2 :- ',l2)

l1[0] = 7777

print('Updated List l1 after updating l1 :- ',l1)
print('Updated List l2 after updating l1 :- ',l2)

l2[1] = 8888

print('Updated List l1 after updating l2 :- ',l1)
print('Updated List l2 after updating l2 :- ',l2)





