# WAP to find number of occourance of each letter in the given string 
word = input('Enter String => ')
print('Word => ',word)
d={}
for ch in word:
	d[ch] = d.get(ch,0)+1
print('Occourance of char =>',d)

for k,v in sorted(d.items()):
	print(k,'occoured',v,'times.')