# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q Best Time to Buy and Sell Stock - II

# You are given an integer array prices where prices[i] is the price 
# of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

# def maxProfit(self, prices: List[int]) -> int:


# S
# sliding window, using two pointer

# iterate using two pointer , set one to day 1 & the other to day 2
# if price at right is higher than left , calculate the profit . then iterate both pointers .

# if right is low or equal , set left pointer to same position as right
def maxProfit(self, prices):
    left , right = 0 , 1
    maxProfit, sumProfit = 0, 0

    while (right < len(prices)):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            # print(prices[right], ' - ', prices[left], ' = ', profit)
            maxProfit += profit
            left += 1
        else:
            left = right
        right += 1

    return maxProfit
