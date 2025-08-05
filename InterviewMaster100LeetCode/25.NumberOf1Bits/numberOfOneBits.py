# https://leetcode.com/problems/number-of-1-bits/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q
# Given a positive integer n, write a function that returns the number of in its
# binary representation (also known as the Hamming weight).


# S
class Solution:
    def hammingWeight(self, n: int) -> int:
        self.count = 0 # set global count

        def getBinary(n): # use recursion until number is non zero
            if n <= 0:
                return
            if n % 2 == 1: # if bit is 1 , then increment count
                self.count += 1 

            n >>= 1 # shift number to right by 1
            getBinary(n)

        getBinary(n)

        return self.count 
