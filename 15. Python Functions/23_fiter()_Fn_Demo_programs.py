# filter(function,sequence)

l = [0,1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda n:n%2==0,l))
print('Even Numbers =>',even)
odd = list(filter(lambda n:n%2!=0,l))
print('Odd Numbers =>',odd)

# NUmbers divisible by 3 and odd
nBy3odd = list(filter(lambda n:n%3==0 and n%2!=0,l))
print('Odd numbers devisible by 3 =>,',nBy3odd)

heroins = ['Katrina Kaif','Kareena Kapoor','Anushka','Deepika','Sunny Leone','Malaika','ABCDE']
startWithK = list(filter(lambda name: name[0]== 'K',heroins))
print("Heroin names starts with 'K' =>",startWithK)

# Name length divisible by 5
lenDivBy5 = list(filter(lambda name: len(name)%5==0,heroins))
print('Name Length divisible by 5 =>',lenDivBy5)

# Name length is odd
OddLen = list(filter(lambda name: len(name)%2!=0,heroins))
print('Name with odd Length =>',OddLen)