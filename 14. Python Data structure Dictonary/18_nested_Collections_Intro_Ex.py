# Nested collection
l1 = [(10,20,30),(40,50,60)] # List of tuples
print('s[1] of 1st tuple =>',l1[0][2])

d = {
	'cars':('Innova','Honda','Maruti'),
	'Mobile':('Samsung','Iphone','Nokia')
	}

# Display 2nd car
print('Second Car =>',d['cars'][1])
print('Second Car =>',d.get('cars')[1])

# Display all mobile names
print('All Mobiles =>',end=' ')
for x in d['Mobile']:
	print(x,end=' ')
print()

