for i in range(3):
	for j in range(3):
		if i == j:
			print('breaked inner loop at {}.'.format(j))
			break
		print('i = {} , j = {}'.format(i,j))

for i in range(3):
	for j in range(3):
		if i == j:
			print('skipped inner loop at {}.'.format(j))
			continue
		print('i = {} , j = {}'.format(i,j))