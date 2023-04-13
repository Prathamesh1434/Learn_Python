# imp fn and methods
# remove() => s.remove(x) => if x not in s => KeyError

s = {10,20,30,40,50}
print('s before remove =>',s)
s.remove(30)
print('s after remove =>',s)
# s.remove(60) => if 60 not in s => KeyError
print()

# discard()
s = {10,20,30,40,50}
print('s before pop =>',s)
s.discard(30)
print('s after pop =>',s)

s.discard(60) # if 60 not in s => No error
print('s after pop =>',s)
print()

# pop() => Removes random element.
s = {10,20,30,40,50}
print('s before pop =>',s)
s.pop()
print('s after pop =>',s)
s.pop()
print('s after pop =>',s)
s.pop()
print('s after pop =>',s)
s.pop()
print('s after pop =>',s)
s.pop()
print('s after pop =>',s)
# s.pop() => KeyError: 'pop from an empty set'

# clear() => Removes all the elements from the set
s = {10,20,30,40,50}
print('s before clear =>',s)
s.clear()
print('s after clear =>',s)