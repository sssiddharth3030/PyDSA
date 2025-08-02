# https://leetcode.com/problems/majority-element/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# S

class Solution:
  # def majorityElement(self, nums: List[int]) -> int:
  def majorityElement(self, nums):
    hashMap = {}

    if len(nums) % 2 == 0:
      target = len(nums) // 2
    else:
      target = (len(nums) // 2) + 1

    # use hashmap to keep track of count
    # if any number is equal or greater than target , return num
    for num in nums:
      if num in hashMap:
        hashMap[num] += 1
        if hashMap[num] >= target:
          return num 
      else:
        hashMap[num] = 1

    # handle edge cases , as there will always be a majority elemennt
    for num, count in hashMap.items():
      if count >= target:
        return num
        