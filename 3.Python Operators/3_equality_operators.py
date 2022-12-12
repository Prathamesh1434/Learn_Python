a = 10
b = 20

print(a == b)
print(a != b)

print(1 == True)

print(10 == 10.0)

print('Prathmesh' == 'Prathmesh')
print(10 == 'Prathmesh')
print(10 == '10')

# Chaining of equality operator
print(10 == 20 == 30 == 40)
print(10 == 10 == 10 == 10)

# '==' and 'is' operator

# '==' => Content comparision
# 'is' => reference conparision
l1 = [10,20,30]
l2 = [10,20,30]
l3 = l1
print('id of l1 :- ',id(l1))
print('id of l2 :- ',id(l2))
print('reference conparision :- ',l1 is l2)
print('reference conparision :- ',l1 is l3)
print('Content comparision :- ',l1 == l2)


