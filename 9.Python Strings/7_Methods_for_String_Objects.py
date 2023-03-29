# Remove the spaces from string.
# lstrip() , rstrip() , strip()
city = input("Enter your city name => ")
# city = input("Enter your city name => ").strip() => This is valid too.

sCity = city.strip()
if sCity == 'Hyderabad':
	print('Hello Hyderabadi.. Aadab !!!')
elif sCity == 'Chennai':
	print('Hello Madrasi .. Vanakkam !!!')
elif sCity == 'Banglore':
	print('Hello Kannadiga .. Namskarm !!!')
else:
	print('Entered city is invalid.')


# Find Substring in string.
#find() , rfind() , index() , rindex()
s = 'ABCBA'
print("'B' is present in string 's' at what index ? => ",s.find('B')) # Search from left side.
print("'B' is present in string 's' at what index ? => ",s.rfind('B')) # Search from right side.
print("'Z' is present in string 's' at what index ? => ",s.find('Z')) # if given substring is not available in string => Then it will return '-1'.

s = 'ABCBEFGHIJBK'
# find('Substring',Begin Index,End Index)
print("'B' is present in string 's' between index 3 to 8 ? => ",s.find('B',3,8)) # Search from left side from 3 to 7.
print("'B' is present in string 's' between index 3 to 8 ? => ",s.rfind('B',3,8)) # Search from right side from 3 to 7.

# Find Subtring in string with index method.
s = 'ABCBA'
print("'B' is present in string 's' at what index ? => ",s.index('B')) # Search from left side.
# print("'Z' is present in string 's' at what index ? => ",s.index('Z')) # if given substring is not available in string => Then it will give ValueError.

mail = input('Enter your mail ID => ')
try:
	i = mail.index('@')
	print("Mail id is valid as it contains '@' Symbol.")
except ValueError:
	print("Mail id is invalid as it does not contains '@' Symbol.")

s = 'ABCDEFGHIJKLMN'
print(s.index('B'))
# print(s.index('B',4,8)) # will search from 4th to 7th index.

s = 'ABCDE'
print(s.index('D',2,100))

# count() method to count the occourance of subString in given string.
s = 'ABBABBABA'
print("count of 'B' in string 's' => ",s.count('B'))
print("count of 'BB' in string 's' => ",s.count('BB'))
print("count of 'BB' in string 's' from 4th to 100th index => ",s.count('BB',4,100))

s = 'BBBBB'
print("count of 'BB' in string 's' => ",s.count('BB'))

print("count of 'BBB' in string 's' => ",s.count('BBB'))
















