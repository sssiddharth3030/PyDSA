# https://leetcode.com/problems/maximum-depth-of-binary-tree/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the 
# longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Traverse the tree using recursion, & keeping track of the level
# store the max using instance attribute
# if root is none , dont set the level
class Solution:
    def __init__(self):
        self.depthMax = 0

    def traverseTree(self, root, level):
        if root is None:
            return

        Solution.traverseTree(self, root.left, level+1)
        Solution.traverseTree(self, root.right, level+1)

        self.depthMax = max(self.depthMax, level)

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    def maxDepth(self, root):
        Solution.traverseTree(self, root, 1)
        return self.depthMax