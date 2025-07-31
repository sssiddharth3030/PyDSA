# https://leetcode.com/problems/binary-search/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums. 

# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# S : standard binary serach with no modifications

# set left to 0, & right to length of nums
# while left pointer is less than right
# calculate mid , check if value of mid == target , if yes return true
# if target greater than nums[mid] then set left to mid +1
# if target less than nums[mid] then set right to mid -1

# default to -1 , as no element found

# def search(self, nums: List[int], target: int) -> int:
def search(self, nums, target):
    left , right = 0, len(nums) - 1

    while(left <= right):
        mid = left + ((right - left) //2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
    
    return -1