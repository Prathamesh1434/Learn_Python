# upper() , lower() , swapcase() , title() , capitalize()
s = 'Learning Python is very easy.'
print('Upper case =>',s.upper())
print('Lower case => ',s.lower())
print('swapcase => ',s.swapcase())
print('title => ',s.title())


# write a program to check whether the given 2 strings are equal or not by ignoring the case.
s1 = input('Enter 1st String => ')
s2 = input('Enter 2nd String => ')

if s1.upper() == s2.upper():
	print('s1 and s2 are equal.')
else:
	print('s1 and s2 are not equal.')

# Write a program to check whether provided username and password are valid or not ? 
# username is not case sensitive , but password should be sensitive.

username = 'Prathmesh.G'
password = 'Munna@1234'

un = input('Enter username => ').lower()
pw = input('Enter password => ')

if un == username.lower() and pw == password:
	print('Valid username and password.')
else:
	print('Username or password is incorrect.')

# Write a programm to convert 1st and last character as upper case and all remaining characters should be lower casr of the given string ?
s1 = input('Enter the String => ')
op = s1[0].upper() + s1[1:len(s1)-1].lower() + s1[-1].upper()
print('string in required format => ',op)

# Checking Starting and ending part of the string. => s.startswith(subString) , s.endsswith(subString)
# Mine
name = 'Prathmesh'
sirname = 'Gayakwad'

s1 = input('Enter the string => ')

if s1[0:len(name)] == name :
	print('Prefix of string is matched.')
else:
	print('Prefix of string is not matched.')

if s1[len(s1)-len(sirname):len(s1)] == sirname :
	print('Sufix of string is matched.')
else:
	print('Sufix of string is not matched.')

print()

if s1.startswith(name):
		print('Prefix of string is matched.')
else:
	print('Prefix of string is not matched.')

if s1.endswith(sirname):
	print('Sufix of string is matched.')
else:
	print('Sufix of string is not matched.')