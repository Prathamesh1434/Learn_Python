# Empty list
l = []
print("Type of l => ",type(l))

# If we know data already.
l = [10,20,30,40]
print("Non empty list => ",l)

l = eval(input("Enter list => "))
print("Type of l => ",type(l))

# By using list() function.
l = list('durga') 
print("List => ",l)

# range to list
l = list(range(0,10,2))
print("List from range => ",l)

# list using split() method.
name = "Prathmesh Jayant Gayakwad"
l = name.split()
print("List after splitting the string => ",l)


