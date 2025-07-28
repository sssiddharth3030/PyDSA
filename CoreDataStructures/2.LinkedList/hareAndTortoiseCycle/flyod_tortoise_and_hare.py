class node():
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None
  pass

head = None
tail = None

def insert_start(data):
  global head, tail
  new_node = node(data)
  
  if head:
    head.prev = new_node
    new_node.next = head
    head = new_node
    return new_node
  else:
    head = new_node  
    tail = new_node
    return new_node
    
def insert_end(data):
  global head, tail
  new_node = node(data)
  
  if tail:
    tail.next = new_node
    new_node.prev = tail
    tail = new_node
    return new_node
  else:
    tail = new_node
    head = new_node
    return new_node
    
def delete_end():
  global head, tail
  
  if tail.prev:
    new_tail = tail.prev
    new_tail.next = None
    tail = new_tail
  else:
    head, tail = None, None
    
def delete_start():
  global head, tail
  
  if head.next:
    new_head = head.next
    new_head.prev = None
    head = new_head
  else:
    head, tail = None, None

def delete(data):
  global head, tail
  
  if head.data == data:
    delete_start()
    return
  elif tail.data == data:
    delete_end()
    return
    
  curr = head
  temp = None
  while(curr):
    if curr.data == data:
      temp = curr.prev
      temp.next = curr.next
      temp.next.prev = temp
      return
    curr = curr.next

def travese_forward():
  global head
  curr = head
  while curr is not None:
    print(curr.data, end=" ")
    curr = curr.next
  print("\n")

def travese_backward():
  global tail
  curr = tail
  while curr is not None:
    print(curr.data, end=" ")
    curr = curr.prev
  print("\n")
  
def reverse_list():
  global head, tail
  
  curr = head
  while curr:
    curr.prev, curr.next = curr.next, curr.prev
    curr = curr.prev
  head, tail = tail, head  
  
#floyd's tortoise & hare circle detection
def is_circle():
  global head

  slow , fast = head , head
  
  while(True):
    slow = slow.next
    
    if fast.next == None or fast.next.next == None:
      return False
    fast = fast.next.next
    
    if slow.data == fast.data:
      find_entrance(slow)
      return slow
    
def find_entrance(meeting_point):
  global head
  
  slow, fast = head, meeting_point
  while ( True ):
    print(slow.data, fast.data)
    if slow.data == fast.data:
      print("Circle Starts at : ", fast.data , end='\n')
      return fast
    slow = slow.next
    fast = fast.next

if __name__ == '__main__':  
  circle_start = insert_start(5)
  insert_start(4)
  insert_start(3)
  insert_start(2)
  insert_start(1)
  insert_end(6)
  insert_end(7)
  insert_end(8)
  insert_end(9)
  insert_end(10)
  delete(8)
  delete_start()

  insert_end(8)
  insert_end(1)
  
  print(is_circle())
  tail.next = circle_start

  print(is_circle().data)

  