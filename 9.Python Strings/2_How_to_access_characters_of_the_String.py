# By Index
# By using Slice

# 1. By Using Index
s = 'Prathmesh'
print(s[0])
print(s[-1])
# print(s[100]) => Index error , String error out of range.

#WAP ri display char. of given string index wise(both positive and negative)
# Mine
s = input("Enter the String => ")

for i in range(len(s)):
	print("index {} => char '{}'".format(i,s[i]))

print()

for i in range(len(s)):
	i += 1
	print("index -{} => char '{}'".format(i,s[-i]))


# Tutor
i = 0
for x in s:
	print('The char present at +ve index : {} and -ve index : {} is : {} .'.format(i,i-len(s),x))
	i += 1



