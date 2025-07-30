#https://leetcode.com/problems/two-sum/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        hashMap = {}
        #one pass solution using hashMap 
        for i in range(len(nums)):
            #store the complement
            complement = target - nums[i]

            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[nums[i]] = i
        
        # Return an empty list if no solution is found
        return []
        
# logic : a + b = target .
# then : b = target - a .
# return index of a & b . index of b is stored using hashMap .