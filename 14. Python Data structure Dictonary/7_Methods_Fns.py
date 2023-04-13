d1 = {100:'A',200:'B',300:'C'}
print('d1 => ',d1)
print('Keys in dict =>',d1.keys())
for k in d1.keys():
	print('Key =>',k)

print('Values =>',d1.values())
for v in d1.values():
	print('Value =>',v)

# k.v => Item
print('Items =>',d1.items())

for i in d1.items():
	print('Item =>',i)

for k,v in d1.items():
	print(k,'_____',v)