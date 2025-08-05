# https://leetcode.com/problems/product-of-array-except-self/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q

# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


# S - using two Array

class Solution:
  # def productExceptSelf(self, nums: List[int]) -> List[int]:
  def productExceptSelf(self, nums):
    n = len(nums)

    l = [1]*n
    r = [1]*n

    # compute left products
    for i in range(1, n):
        l[i] = l[i-1]* nums[i-1]

    # compute right products
    for i in range(n -2 , -1, -1):
        r[i] = r[i+1] * nums[i+1]

    # compute answer, multiply the product of left & right for each position at nums
    a = [ l[i] * r[i] for i in range(n) ]
        
    return a