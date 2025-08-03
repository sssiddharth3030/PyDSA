# A heap is a complete binary tree data structure .
# The last level will be filled from left .

# Max-Heap , the parent nodes should be greater than leaf nodes.
# Min-Heap , the child nodes should be lesser than leaf nodes .

# reference: 
# https://www.youtube.com/watch?v=E2v9hBgG6gE
# https://medium.com/@hs_pedro/implementing-a-heap-in-python-1036e759e0eb
# left child index: 2*k + 1
# right child index: 2*k + 2
# parent index: k /2 (taking the floor)

import heapq

# HeapSort
# Time: O(n log n), Space: O(n)
# Note: O(1) Space is possible via swapping, but this is more complex
def heapSort(arr):
  heapq.heapify(arr)
  n = len(arr)
  newList = [0] * n
  
  for i in range(n):
    newList[i] = heapq.heappop(arr)
  
  return newList

# turn min heap to max heap & vice-versa
def maxHeap(arr):
  for i in range(len(arr)):
    arr[i] *= -1
  
  heapq.heapify(arr)

# Heap Push (Insert element)
# Time: O(log n)
def heapPush(arr, data):
  heapq.heappush(arr, data)

# Heap Pop (Extract min)
# Time: O(log n)
def heapPop(arr):
  heapq.heappop(arr)

if __name__ == '__main__':
  A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
  print("Array: ")
  print(A)
  
  # turn the array, into a min heap
  heapq.heapify(A)
  print("Array after Heapify: ")
  print(A)
  
  # let's add elements to heap
  heapPush(A, 11)
  heapPush(A, -11)
  heapPush(A, 15)
  
  print("New elements added to Heap: ")
  print(A)
  
  # let's do a heap sort
  A = heapSort(A)
  print('After Heap Sort: ')
  print(A)
  
  # peek on min heap
  print('min value in heap: ', A[0])
  
  # turn the heap into a max heap
  maxHeap(A)
  print("After turning into Max Heap")
  print(A)
  
  # pop, push & peek at max heap
  heapPop(A)
  heapPush(A, 7 * -1)
  heapPush(A, -6 * -1)
  print("Max Heap , after push & pop: ")
  print(A)
  
  print('max value in heap: ', -A[0])