# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q
# Given a 1-indexed array of integers numbers that is already sorted 
# in non-decreasing order, find two numbers such that they add up 
# to a specific target number. Let these two numbers be numbers[index1] 
# and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, 
# added by one as an integer array [index1, index2] of length 2.

# def twoSum(self, numbers: List[int], target: int) -> List[int]:

def twoSum(self, numbers, target):
    # set one pointer at start & one at end of list
    # if the sum of the low & high equals, return indices
    
    # if the sum is less than target, increment low by 1
    # if the sum is greater than target , decrement high by 1
    
    # keep moving high or low , till you find target
    low, high = 0 , len(numbers) - 1
    while low < high:
        print(numbers[low], ' + ', numbers[high], ' = ', numbers[low]+numbers[high])
        if numbers[low] + numbers[high] == target:
            return [low+1, high+1]
        if numbers[low] + numbers[high] < target:
            low += 1
        if numbers[low] + numbers[high] > target:
            high -= 1
        return []