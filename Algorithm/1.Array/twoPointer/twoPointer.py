#Two-Pointer Technique - O(n) time and O(1) space

# The idea of this technique is to begin with two corners of the given array. 
# We use two index variables left and right to traverse from both corners.

# Initialize: left = 0, right = n - 1, then run the loop

#let's try a sample 2 sum problem , with sorted array

def twoSum(arr, target):
  left = 0
  right = len(arr) - 1
  
  while left<right:
    sum = arr[left] + arr[right]

    if sum == target:
      print(arr, f'arr[{left}]+arr[{right}] = {arr[left]} + {arr[right]} = {sum}, target found.')
      return True
    elif sum < target:
      left += 1
    elif sum > target:
      right -= 1
  
  print(arr, target, 'target not found.')
  return False

if __name__ == '__main__':
  twoSum([-3, -1, 0, 1, 2], -2)
  twoSum([-3, -1, 0, 1, 2], 0)
  twoSum([-3, -1, 0, 1, 2], 5)