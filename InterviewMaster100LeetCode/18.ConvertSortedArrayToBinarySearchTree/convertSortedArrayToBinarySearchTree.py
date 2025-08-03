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
        
class Solution:
  def __init__(self):
    pass
  # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
  def sortedArrayToBST(self, nums):
    def helper(l, r):
      if l > r:
        return None

      m = l + ((r - l)//2 )
      root = TreeNode(nums[m])
      root.left= helper(l, m-1)
      root.right = helper(m+1, r)

      return root

    return helper(0, len(nums) - 1)