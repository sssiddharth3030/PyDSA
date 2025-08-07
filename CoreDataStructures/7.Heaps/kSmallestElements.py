import heapq

if __name__ == '__main__':
  A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
  
  heapq.heapify(A)
  K = 5
  
  print(A)
  print(A[:K])
  
  