# https://leetcode.com/problems/single-number/submissions/1719564566/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q
# Given a non-empty array of integers nums, 
# every element appears twice except for one. 

# Find that single one.

# You must implement a solution with a linear runtime complexity 
# and use only constant extra space.

# S
# use XOR operation to find the number without duplicates
# A XOR A = 0 in binary , given only one number without duplicates,
# the result of XOR will be that number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        n = 0
        for num in nums:
            n = num ^ n

        return n 