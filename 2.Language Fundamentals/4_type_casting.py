# 1. any to int()

f = 123.342
print('Float to Int :- ',int(f))

c = 10 + 5.5j  # => int(c) => Not Possible 

b1 = True
b2 = False
print('Boolean to Int : - ',int(b1))
print('Boolean to Int : - ',int(b2))

s1 = '10'
s2 = '10.5'   # int(s2) => Not Possible
s3 = 'Ten'    # int(s3) => Not Possible
s4 = '0B1101' # int(s4) => Not Possible

print('String to Int :- ',int(s1))

# 2. any to float

i = 10
print('Int to Float :- ',float(i))

c = 10 + 5.5j  # => float(c) => Not Possible 

b1 = True
b2 = False
print('Boolean to Int : - ',float(b1))
print('Boolean to Int : - ',float(b2))

s1 = '10'
s2 = '10.5'   
s3 = 'Ten'    # float(s3) => Not Possible
s4 = '0B1101' # float(s4) => Not Possible


print('String to Int :- ',float(s1))
print('String to Int :- ',float(s2))

# 3. any to complex
print('Form 1')
i = 10
print('Int to Complex :- ',complex(i))

f = 10.5
print('Float to Complex :- ',complex(f))

b1 = True
b2 = False
print('Boolean to Complex :- ',complex(b1))
print('Boolean to Complex :- ',complex(b2))

s1 = '10'
s2 = '10.5'
s3 = 'Ten' # => complex(s3) => Not Possible

print("String to Complex :- ",complex(s1))
print("String to Complex :- ",complex(s2))

print('Form 2')

i = 10
f = 2.2
print('Int as real & Float as img :- ',complex(i,f))

b1 = True
b2 = False
print('b1 as real & b2 as img :- ',complex(b1,b2))

s1 = '10'
s2 = '10.5' # => complex(s1,s2) => Not Possible for Form 2

# 4. any to bool
i = 0
i1 = 1 
i2 = 20

f = 0.0
f1 = 10.2
f2 = 11.2

c = 0 + 0j
c1 = 1.2 + 0j
c2 = 0 + 2.3j

s = ''
s1 = 'True'
s2 = 'False'

print('Int[Zero] to Boolean :- ',bool(i))
print('Int[Non Zero] to boolean :- ',bool(i1))
print('Int[Non Zero] to boolean :- ',bool(i2))

print('Float[Zero] to Boolean :- ',bool(f))
print('Float[Non Zero] to boolean :- ',bool(f1))
print('Float[Non Zero] to boolean :- ',bool(f2))

print('Complex[Zero,Zero] to Boolean :- ',bool(c))
print('Complex[Non Zero,Zero] to boolean :- ',bool(c1))
print('Complex[Zero,Non Zero] to boolean :- ',bool(c2))

print('String[Empty] to Boolean :- ',bool(s))
print('String[Non Empty] to boolean :- ',bool(s1))
print('String[Non Empty] to boolean :- ',bool(s2))

# 5. any to string
i = 10
f = 2.2
c = 1.2 + 2.2j
b = True

print('Int to String :- ',str(i))
print('Float to String :- ',str(f))
print('Complex to String :- ',str(c))
print('Boolean to String :- ',str(b))








