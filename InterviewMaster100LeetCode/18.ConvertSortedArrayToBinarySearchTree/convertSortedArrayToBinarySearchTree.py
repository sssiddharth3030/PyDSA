# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q
# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height balanced binary search tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# S - recursion to construct the tree        
class Solution:
  def __init__(self):
    pass
  # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
  def sortedArrayToBST(self, nums):
    def helper(l, r):
      # base case
      if l > r:
        return None
      
      # we are starting at mid , since sorted array

      m = l + ((r - l)//2 )
      # create node for the value
      root = TreeNode(nums[m])
      # create left tree
      root.left= helper(l, m-1)
      # create right tree
      root.right = helper(m+1, r)

      # return root
      return root

    return helper(0, len(nums) - 1)