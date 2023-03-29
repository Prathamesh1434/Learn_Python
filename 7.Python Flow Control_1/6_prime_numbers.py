# programm based on Prime numbers 
#WAP to check the given number is prime number or not ?
#WAP to generate prime number which are less than or equal the given number ?
#WAP to generate first n prime numbers.

# program based on Prime numbers 
#WAP to check the given number is prime number or not ?
#Mine

n = int(input('Enter the Number :- '))
k = 0
for i in range(n):
    if n%(i+1)==0:
        k+=1
        if k>2:
            print('{} is not prime number.'.format(n))
            break
    
if k == 2:
    print('{} is prime number.'.format(n))


print()

#tutor
if n<= 1 :
	print("It is not the prime number.")
else:
	is_prime = True

for i in range(2,n//2+1):
	if n%i == 0 :
		is_prime = False
		break

if is_prime == True :
	print('{} is prime number.'.format(n))
else:
	print('{} is not prime number.'.format(n))


#WAP to generate prime number which are less than or equal the given number ?
#Mine
prime_no_list = []
v = 1
k = 0


while len(prime_no_list) < 10:
    v += 1
    for m in range(v):  
        if v%(m+1)==0:  
            k+=1         
            if k>2:
                print('{} is not prime number.'.format(v))
                break
    if k == 2 :
        prime_no_list.append(v)    
        print('{} added to the list of prime number.'.format(v))
    k = 0
        
print('1st 10 prime numbers :- ',prime_no_list)

print()
# tutor
n1 = 2
while n1 <= n:
	#code to check that , n1 is prime or not.
	is_prime = True
	for i in range(2,n1//2+1):
		if n % i == 0:
			is_prime = False
			break

	if is_prime == True:
		print('{} is prime number.'.format(n1))
	n1 += 1



#WAP to generate first n prime numbers.
#Mine
prime_num_req = int(input("How many prime numbers required ? \n Ans => "))

prime_no_list = []
v = 1
k = 0


while len(prime_no_list) < prime_num_req:
    v += 1
    for m in range(v):  
        if v%(m+1)==0:  
            k+=1         
            if k>2:
                print('{} is not prime number.'.format(v))
                break
    if k == 2 :
        prime_no_list.append(v)    
        print('{} added to the list of prime number.'.format(v))
    k = 0
        
print('1st {} prime numbers :- '.format(prime_num_req),prime_no_list)

#Tutor
count = 0
n1 = 2

while True :
	is_prime = True
	for i in range(2,n1//2+1):
		if n1 % i == 0:
			is_prime =  False
			break

	if is_prime == True:
		print(n1)
		count += 1

	if count == n:
		break
	n1 = n1 + 1

