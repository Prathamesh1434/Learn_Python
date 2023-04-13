# Access elements of tuple
# By index
t = (10,20,30,40,50)
print('Element at index 0 => ',t[0])
print('Element at index -1 => ',t[-1])
print('Element at index 1 => ',t[1])
print('Element at index -3 => ',t[-3])
# print(t[100]) => index error

print()
t = (10,20,30,40,50,60,70,80)
print('elements from 2 o 4 => ',t[2:5]) # (30, 40, 50)
print('elements => ',t[::2]) # (10, 30, 50, 70)