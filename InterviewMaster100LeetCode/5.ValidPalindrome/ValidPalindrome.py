# https://leetcode.com/problems/valid-palindrome/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.

# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# S

# using regex to remove non-alpha numeric values. set string to lower case.
# now use a two pointer , compare first & last pointers ,
# if not same , return false
# if not differences between left & right , then returns true

import re

# def isPalindrome(self, s: str) -> bool:
def isPalindrome(self, s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    print(s)

    left , right = 0, len(s)-1

    while (left < right):
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
