# to provide o/p to console we need to use print statement.

# 1
print("Prathmesh Gayakwad")
print() # provides new line char.
print('Dnyanesh Gayakwad')

# 2
print('PrathmeshGayakwad')
print('Prathmesh\nGayakwad')
print('Prathmesh\tGayakwad')

# 3
print('Prathmesh'+'Engg')
print(10*'Munna')

# 4
a,b,c = 10,20,30
print("Values are :",a,b,c)

# 5 'sep' attribute
a,b,c,d = 10,20,30,40
print('values :-',a,b,c,d) # 10 20 30 40
print('Values using seprator :-',a,b,c,d,sep =':')

# 6 'end' attribute
print('hello')
print('durga')
print('soft')

print('hello',end='')
print('durga',end='')
print('soft')

print('hello',end='::')
print('durga',end='***')
print('soft')

# ex with sep and end attribute
print(10,20,30,sep=':',end='***')
print(40,50,60,sep=':')
print(70,80,sep='**',end='$$')
print(90,100)

# ex
print('Prathmesh','Gayakwad')
print('Prathmesh'+'Gayakwad')

# 7 'replacement' operator {}

#print(any object is possible)

l = [10,20,30,40]
print('list :',l)

t = (10,20,30,40)
print('tuple :',t)

name = 'Prathmesh'
salary = 1000
gf = 'Tummy'

print('Hello {}, Your salary is {}, your friend {} is waiting.'.format(name,salary,gf))
print('Hello {0}, Your salary is {1}, your friend {2} is waiting.'.format(name,salary,gf))
print('Hello {name}, Your salary is {salary}, your friend {gf} is waiting.')
print('Hello {n}, Your salary is {s}, your friend {f} is waiting.'.format(n = name,s = salary , f = gf))

a,b,c,d = 10,20,30,40
print('a = {} , b = {} , c = {} , d = {} '.format(a,b,c,d))

# 8 print with formatted string

# %i => signed decimal value
# %d => signed decimal value
# %f => float value
# %s => String , any other objects list , set ...

a = 10
# print("formatted String" %(variable list))
print('a value : %i' %a)

a = 10 
b = 20
c = 30
print('a = %d , b = %d , c = %d' %(a,b,c))

name = 'Prathmesh'
marks = [10,20,30,40]

print('Hello %s, your marks list : %s' %(name,marks))

# Ex
price = 70.567966
print("price value = {}".format(price))
print("price value = %f" %price)
print("price value = %.2f" %price)











