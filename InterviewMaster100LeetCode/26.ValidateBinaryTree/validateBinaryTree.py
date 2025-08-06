# https://leetcode.com/problems/validate-binary-search-tree/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left #of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# S

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def isValidBST(self, root):
        # Helper function to perform DFS traversal
        # It takes a node and the valid range (left, right) that this node's value must lie within
        def dfs(node, left, right):
            if not node:
                # An empty node/subtree is always valid
                return True

            # The current node's value must be strictly between left and right bounds
            if not (left < node.val < right):
                return False

            # Recursively validate left and right subtrees
            # Left subtree: values must be less than current node's value
            # Right subtree: values must be greater than current node's value
            return (
                dfs(node.left, left, node.val) and
                dfs(node.right, node.val, right)
            )

        # Start the recursion with the entire range of possible values
        return dfs(root, float("-inf"), float("inf"))