# FIFO - First In, First Out

def enqueue(queue, data):
  queue.append(data)

def dequeue(queue):
  if queue:
    queue.pop(0)
  return None

queue = []
enqueue(queue, 1)
enqueue(queue, 2)
enqueue(queue, 3)
enqueue(queue, 4)
enqueue(queue, 5)

print(queue)

dequeue(queue)
dequeue(queue)

print(queue)