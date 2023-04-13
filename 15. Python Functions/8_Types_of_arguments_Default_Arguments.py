# Default Argument

def wish(name='Guest'): # Valid
	print('Hello',name,'Good Evening !!!')

wish('Prathmesh')
wish() # Default value will be considered.

def wish(name,msg): # Valid
	print('Hello',name,msg)

def wish(name='Guest',msg='Good Morning !'): # Valid
	print('Hello',name,msg)

def wish(name,msg='Good Morning !'): # Valid
	print('Hello',name,msg)

# def wish(name='Guest',msg): Error => After default argument , we can't take non default argument.
# 	print('Hello',name,msg)