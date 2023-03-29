# Checkiing Type of characters present in the given String.
# s.isalnum() => [a to z , A to Z , 0 to 9] 
# s.isalpha() 
# s.islower()
# s.isupper()
# s.isdigit()
# s.istitle()
# s.isspace()

print('Durga786'.isalnum())
print('Durga786'.isalpha())
print('Durga'.isalpha())
print('Durga'.isdigit())
print('786786'.isdigit())
print('abc'.islower())
print('Abc'.islower())
print('abc123'.islower())
print('ABC'.isupper())
print('Prathmesh Jayant Gayakwad'.istitle())
print('Prathmesh jayant gayakwad'.istitle())
print('     '.isspace())

# Write a programm to check the type of character entered from the keyboard ?
s = input('Enter the character => ')

if s.isalnum():
	print('It is isalpha Numeric character.')
	if s.isalpha():
		print('It is alphabate character.')
		if s.islower():
			print('It is lower case alphabate symbol.')
		else:
			print('It is upper case alphabate symbol.')
	else:
		print('It is digit.')
elif s.isspace():
	print('It is space character.')
else:
	print('It is non-space special character.')
