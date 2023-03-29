# + => Concatination
# * => Repitation

print('durga'+'classes')
print('durga' * 3)
# print('durga' * 3.0) => will give error as 3.0 is float value

# Membership operator
s = 'Prathmesh'
print("'P' in Prathmesh ? ",'P' in s)
print("'ath' in Prathmesh ? ",'ath' in s)
print("'es' in Prathmesh ? ",'P' in s)
print("'zx' in Prathmesh ? ",'zx' in s)

s = input('Enter main string => ')
sb = input ('Enter subString => ')

if sb in s:
	print("Substring '{}' present in main string '{}'.".format(sb,s))
else:
	print("Substring '{}' not present in main string '{}'.".format(sb,s))

# Comparision operators for strings: (< , <= , > , >= , == , !=) 
print("'durga' < 'ravi' => ",'durga' < 'ravi') # this comparison is based on unicode value
print("unicode of 'd' => ",ord('d'))
print("unicode of 'r' => ",ord('r'))

print("'ramba' < 'ramya' => ",'ramba' < 'ramya')

s1 = input('Enter 1st String => ')
s2 = input('Enter 2nd String => ')

if s1 == s2:
	print("Both Strings are equal.")
elif s1 < s2:
	print("First String is less than second one.")
else:
	print("Second String is less than first one.")









