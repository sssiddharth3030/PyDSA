# https://leetcode.com/problems/maximum-subarray/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q Maximum Subarray
# Given an integer array nums, find the with the largest sum, 
# and return its sum.

# S
class Solution:
  # def maxSubArray(self, nums: List[int]) -> int:
  def maxSubArray(self, nums):
    maxx = nums[0]
    curr = 0

    for n in nums:
      # if the current sum is negative , reset it
      if curr < 0:
        curr = 0

      curr += n
      maxx = max(maxx, curr)

    return maxx
