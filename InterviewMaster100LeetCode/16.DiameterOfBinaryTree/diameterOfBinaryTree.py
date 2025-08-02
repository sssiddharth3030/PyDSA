# https://leetcode.com/problems/diameter-of-binary-tree/submissions/1720134019/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q
# Given the root of a binary tree, return the 
# length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between 
# any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented 
# by the number of edges between them.

# S
# Definition for a binary tree node.

# refer Neetcode for explanation : https://www.youtube.com/watch?v=K81C31ytOZE
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
  def diameterOfBinaryTree(self, root):
    self.res = 0
    # use recursion to find the diameter of current node , 
    # if it is larger than update the maximum diameter
    def dfs(curr):
      if not curr:
        return 0

      left = dfs(curr.left)
      right = dfs(curr.right)

      self.res = max(self.res, left+right)
      return 1 + max(left, right)

    dfs(root)
    return self.res