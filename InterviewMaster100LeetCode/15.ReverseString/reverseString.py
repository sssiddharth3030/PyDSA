# https://leetcode.com/problems/reverse-string/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q Reverse String

# Write a function that reverses a string. 
# The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# S

class Solution:
  # def reverseString(self, s: List[str]) -> None:
  def reverseString(self, s):
    """
    Do not return anything, modify s in-place instead.
    """
    low, high = 0, len(s) - 1

    while(low <= high):
      s[low], s[high] = s[high], s[low]
      low += 1
      high -= 1