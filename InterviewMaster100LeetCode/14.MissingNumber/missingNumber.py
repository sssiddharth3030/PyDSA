# https://leetcode.com/problems/missing-number/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.


# S
class Solution:
  # def missingNumber(self, nums: List[int]) -> int:
  def missingNumber(self, nums):
    length , sumTotal = len(nums), 0
    # get the sum of all elements , for array length .
    maxSum = length * (length + 1) // 2

    # get the sum of all elements in array
    for num in nums:
      sumTotal += num

    # the difference , is the missing number
    return maxSum - sumTotal