# Write a program to generate fake Employee data for database Testing 
# 1 Emp Name => 
# 2 Emp Number => e-1234
# 3 Emp Salary => 10000 to 50000
# 4 Emp City => ['Hyderabad','Chennai','Banglore','Pune','Delhi','Mumbai']
# 5 Emp Mobile Number => 9898964666
# 6 Designation

from random import *
alphabates = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
cities = ['Hyderabad','Chennai','Banglore','Pune','Delhi','Mumbai']
designation = ['Software Engg','Senior software Engg','Team Lead','Project Lead','Project Manager']

def getFakeName():
	name = choice(alphabates).upper()
	n = randint(2,9)
	for i in range(n):
		name = name+choice(alphabates)
	return name

print('Name =>',getFakeName())

def getFakeEnum():
	eNum = 'e-'
	for i in range(4):
		eNum = eNum+choice(digits)
	return eNum

print('Emp Num =>',getFakeEnum())

def getFakeSalary():
	eSal = uniform(10000,50000)
	return eSal

print('The Salary =>',getFakeSalary())

def getFakeCity():
	city = choice(cities)
	return city

print('The City =>',getFakeCity())

def getFakeDesignation():
	desig = choice(designation)
	return desig
print('The designation =>',getFakeDesignation())

def getFakeMnum():
	mNo = choice('6789')
	for i in range(9):
		mNo = mNo + choice(digits)
	return mNo

print('Mobile Number =>',getFakeMnum())
print()
def getFakeEmpData():
	print('Name =>',getFakeName())
	print('Emp Num =>',getFakeEnum())
	print('The Salary =>{:.2f}'.format(getFakeSalary()))
	print('The City =>',getFakeCity())
	print('Mobile Number =>',getFakeMnum())
	print('The designation =>',getFakeDesignation())

getFakeEmpData()

for i in range(10):
	getFakeEmpData()
	print()