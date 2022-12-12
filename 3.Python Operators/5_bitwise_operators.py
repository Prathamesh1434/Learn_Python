# '&' => Bitwise and
# '|' => Bitwise OR
# '^' => Bitwise X-OR
# '~' => Bitwise complement operator
# '<<' => Bitwise left-shift operator
# '>>' => Bitwise right-shift operator

# Only for int and boolean
# 10.5 & 20.6 => Gives TypeError
# 'Prathmesh' & 'Prathmesh' => Gives TypeError

# 1. & , | , ^
print(4 & 5) # => Both bits are one , then result is 1. otherwise 0.
print(4 | 5) # => Atleast one bit is one , then result is 1. otherwise 0.
print(4 ^ 5) # => Both bits are different , then result is 1. otherwise 0.

# 2. " ~ "
print('Negation of 4 :- ',~4) # 4 = 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
             # 1st Step [0 <=> 1] = 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | => Start's with 1 => -ve number => and exclude it while adding 1. that's why * is added.
      # 2nd Step [1's Complement] = * | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
                               #  +                                                                                                                           | 1 |
                               #  ---------------------------------------------------------------------------------------------------------------------------------
               # [2's Complement] = * | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | => 5
                   # Therefore ~4 = -5

print('Negation of 5 :- ',~5)
print('Negation of -4 :- ',~-4)

# 3. "<<" and ">>"
print('Left shift 10 by 2 :- ',10 << 2) # 10 = 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
                                    # Step 1 = ^   ^
                                    # These 2 zero will gone. And two vacent cell will be created at the end of the number.
                              # Final Result = 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
                   # Added zero's at the end =                                                                                                                         ^   ^

print('Right shift 10 by 2 :- ',10 >> 2)  # 10 = 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
                                      # Step 1 =                                                                                                                         ^   ^
                                      # These 2 zero will gone. And two vacent cell will be created at the start of the number.
                                # Final result = 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
 # Added zero's at the begining of the number  = ^   ^
 #as 10 is +ve.

# Ex on boolean type.
print(True & False)
print(True | False)
print(True ^ False)
print(True << False)
print(True >> False)
print(True & True)
print(True | True)
print(True ^ True)
print(True << True)
print(True >> True)

print(~True)
print(~False)


