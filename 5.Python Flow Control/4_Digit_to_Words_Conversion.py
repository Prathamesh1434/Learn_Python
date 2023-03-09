# WAP to take a single digit number from the keyboard and print its value in words

n = int(input('Enter any digit from 0 to 9 : '))

if n == 0:
	print('ZERO')
elif n == 1:
	print('ONE')
elif n == 2:
	print('TWO')
elif n == 3:
	print('THREE')
elif n == 4:
	print('FOUR')
elif n == 5:
	print('FIVE')
elif n == 6:
	print('SIX')
elif n == 7:
	print('SEVEN')
elif n == 8:
	print('EIGHT')
elif n == 9:
	print('NINE')
else:
	('Number is not between 0 to 9')

print('------------------------------------')

words = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
if n>=0 and n<=9:
	print(words[n])

print('------------------------------------')

words_upTo_19 = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine''Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
words_for_10 = ['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty']

n = int(input('Enter Number from 0 to 99 : '))

output = ''

if n == 0 :
	output = 'Zero'
elif n <=19:
	output = words_upTo_19[n]
elif n<=99:
	output = words_for_10[n//10] + ' ' + words_upTo_19[n%10]
else:
	output = 'Please enter a value between 0 to 99.'

print(output)
