# stack is LIFO - Last in, First Out

#peek - look at top most element without removing it
def peek(stack):
  if stack:
    return stack[-1]
  return None
  
stack = []

# add elements to end
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')

print(stack)
print(peek(stack))

#remove elements from end
stack.pop()
stack.pop()

print(stack)
print(peek(stack))

