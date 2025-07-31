# https://leetcode.com/problems/valid-anagram/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Given two strings s and t, return true if t is an anagram
# of s, and false otherwise.

# An anagram is a word or phrase formed by rearranging the letters 
# of a different word or phrase, using all the original letters 
# exactly once.

# S1
# using hashMap to store the count of alphabets from s
# reduce the count comparing t , if 0 pop the character
# if an alphabet not in hashmap is found in t , return false
# if hashmap is not empty at end , it is not an anagram, return false
# else return true as default

def isAnagram(self, s: str, t: str) -> bool:

    hashMap = {}

    if len(s) != len(t):
        return False

    for c in s:
        if c in hashMap:
            hashMap[c] += 1
        else:
            hashMap[c] = 1

    for c in t:
        if c in hashMap:
            hashMap[c] -= 1
        if hashMap[c] <= 0:
            hashMap.pop(c)
        else:
            return False

    if hashMap:
        return False
    return True