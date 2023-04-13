# empty dict
d = {}
d = dict()
print('dict d =>',d)

# if you aware abt data
d = {100:'Durga',200:'Ravi'}
print('dict d =>',d)
print()

# by using dict()
l = [(100,'A'),(200,'B'),(300,'c')] # list of tuples
d = dict(l)
print('dict d from list of tuples =>',d)
print()
# set of list or tuple of list => we can't convert this two collection to dict as list unhashable.
# internal element should contain only two element , otherwise it will give error.

# By using dynamic input
d = eval(input('Enter dictonary => '))
print('dict d =>',d)