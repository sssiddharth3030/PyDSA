# https://leetcode.com/problems/climbing-stairs/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways 
# can you climb to the top?

# S
class Solution:

  def climbStairs(self, n: int) -> int:
    # Create a dictionary to store previously computed results (memoization)
    memo = {}
    # Define a helper function that does the actual recursion
    def helper(i):
      nonlocal memo
      # Base case: If there are 0 or 1 steps, there's only 1 way to climb
      if i== 0 or i == 1:
        return 1
      # If we’ve already computed the result for i steps, return it from memo
      if i in memo:
        return memo[i]
      
      # Otherwise, compute the result recursively and store it in memo
        # The number of ways to climb 'i' steps is the sum of:
        # - ways to climb (i-1) steps, then take 1 step
        # - ways to climb (i-2) steps, then take 2 steps
      memo[i] = helper(i - 1) + helper( i - 2)
      
      # Return the computed value
      return memo[i]
    # Start the recursion from step 'n'
    return helper(n)

    # naive approach
    # It uses the recurrence relation:
      #   ways(n)=ways(n−1)+ways(n−2)
      #   ways(n)=ways(n−1)+ways(n−2)
      # Which resembles the Fibonacci sequence.
      
    # if n == 0 or n == 1:
    #   return 1
    # return self.climbStairs(n-1) + self.climbStairs(n-2)