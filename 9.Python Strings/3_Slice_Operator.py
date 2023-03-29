# slice operator for substring.
# [begin : end ] => returns sub string from begin index to end - 1 index.
#				 => begin index is optional and default value is 0.
#				 => end index is optional and default value is len(s).

s = 'abcdefghijk'

print(s[2:7])
print(s[:7])
print(s[2:])
print(s[:])

# [begin : end : Step] => default value for step is 1.
#					   

s = 'abcdefghijk'
print(s[2:7]) 
print(s[2:7:1]) # line 17 = line 18
print(s[2:7:2]) 
print(s[2:7:3]) 
print(s[::2]) 


