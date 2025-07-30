# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the
# price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day
# to buy one stock and choosing a different day in the future
# to sell that stock.

# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# def maxProfit(self, prices: List[int]) -> int:


# S
# sliding window using two pointer

# iterate using two pointer
# if price at right is higher than left , calculate the profit
# and update maxprofit if it's greater . 

# if right is low or equal , set left pointer to same position as right

def maxProfit(self, prices):
    left, right = 0, 1
    maxProfit = 0

    while (right < len(prices)):
        if prices[right] > prices[left]:
            sumProfit = prices[right] - prices[left]
            maxProfit = max(maxProfit, sumProfit)
        else:
            left = right
        right += 1

    return maxProfit
