l = [10,20,30,40]

# By using index.
print("1st element => ",l[1])
print("Last element => ",l[-1])
# print(l[100]) # index error.

# By using slice operator.
# list = l[begin:end:step] => Step (+ve) => forward direction , begin to end-1 | Step (-ve) => backward direction , begin to end+1

l = [10,20,30,40,50,60,70,80,90,100]
print(l[2:7]) # [30,40,50,60,70]
print(l[2:7:2]) #[30,50,70]
print(l[4::2]) # [50,70,90]
print(l[8:2:-2]) # [90,70,50]
print(l[4:100]) # [50,60,70,80,90,100]
print(l[4:0:2]) # l[]

print(l[::1])
print(l[::-1])