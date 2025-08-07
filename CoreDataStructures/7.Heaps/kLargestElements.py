import heapq

def maxHeap(arr):
  for i in range(len(arr)):
    arr[i] *= -1

    heapq.heapify(arr)

if __name__ == '__main__':
  A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
  
  heapq.heapify(A)
  K = 5
  
  maxHeap(A)
  
  TK = [ -heapq.heappop(A) for i in range(K)]
  
  print(TK)