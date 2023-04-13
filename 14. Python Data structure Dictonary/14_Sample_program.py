# WAP to find number of occourace of each vowel in the string.
word = input('Enter String => ')
print('Word => ',word)
vowels = {'a','e','i','o','u'}
d = {}
for ch in word:
	if ch in vowels:
		d[ch] = d.get(ch,0)+1
print('Occourance of vowel =>',d)

for k,v in sorted(d.items()):
	print(k,'occoured',v,'times.')