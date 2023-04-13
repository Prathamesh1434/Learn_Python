vowels = ['a','e','i','o','u']

s = input("Enter the String => ")
result = []
for ch in s:
	if ch in vowels:
		if ch not in result:
			result.append(ch)

print('Vowels in string => ',result)
print('The number of unique vowels => ',len(result))
print()

result1 = []
for ch in vowels:
	if ch in s:
		result1.append(ch)
print('Vowels in string => ',result1)
print('The number of unique vowels => ',len(result1))

print()

result2 = []
result2 = [ch for ch in vowels if ch in s] 
print('Vowels in string => ',result2)
print('The number of unique vowels => ',len(result2))