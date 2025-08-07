# https://leetcode.com/problems/house-robber/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint 
# stopping you from robbing each of them is that adjacent houses 
# have security systems connected and it will automatically contact 
# the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

# S - Dynamic Programming
class Solution:
    # def rob(self, nums: List[int]) -> int:
    def rob(self, nums):
        # If the list is empty, there are no houses to rob
        if not nums:
            return 0

        # If there's only one house, rob it
        if len(nums) == 1:
            return nums[0]

        n = len(nums)

        # Create a list to store the maximum money that can be robbed up to each house
        max_money = [0] * n

        # Base case: the maximum money after the first house is just robbing it
        max_money[0] = nums[0]

        # Base case: the maximum after the second house is the max of robbing the first or second
        max_money[1] = max(nums[0], nums[1])  # Corrected the typo here

        # Loop through the rest of the houses
        for i in range(2, n):
            # At each step, decide whether to rob the current house (and add to the total two steps before)
            # or skip it and take the max money from the previous house
            max_money[i] = max(
                max_money[i - 1],             # Don't rob current house
                nums[i] + max_money[i - 2]    # Rob current house + money from i-2
            )  # Corrected the typo here as well

        # The last element in max_money contains the answer
        return max_money[-1]
        