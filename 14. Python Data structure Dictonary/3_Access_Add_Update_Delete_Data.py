d = {100:'Durga',200:'Ravi',300:'Prathmesh'}
print('dict d =>',d)
print('value for key 100 =>',d[100])
print('value for key 300 =>',d[300])
# print('value for key 700 =>',d[700]) => KeyError: 700 as key is not available in dictonary.
key = int(input('Enter the key to find the corresponding value => '))
if key in d:
	print('value for key {} => {}'.format(key,d[key]))
else:
	print('specifed key {} not in dict.'.format(key))

print()
# How to add / update the data in dict
print('dict d =>',d)
d[100] = 'Moti'
print('dict d =>',d)
d[400] = 'Jayant'
print('dict d =>',d)
print()

# How to delete data from dict
print('dict d =>',d)
del d[200] # if key is not available in dict => KeyError
print('dict d =>',d)
del d[100],d[300]
print('dict d =>',d)