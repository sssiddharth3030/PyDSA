# https://leetcode.com/problems/valid-parentheses/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.


# def isValid(self, s: str) -> bool:
def isValid(self, s):
    #keep a hasmap for closing to open parentheses
    hashMap = {
            ")": "(",
            "}": "{",
            "]": '['
            }

    # use a stack to store the open parentheses
    stack = []

    for c in s:
        if c in hashMap:
            # if stack is not empty , 
            # then peek to see if the closing parentheses is the correct one for it
            
            #if not there is a mismatch , return False
            if stack and (stack[-1] == hashMap[c]):
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    #if stack is not empty , then there is a mismatch
    if stack:
        return False
    return True