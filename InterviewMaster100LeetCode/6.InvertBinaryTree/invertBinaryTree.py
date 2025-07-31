# https://leetcode.com/problems/invert-binary-tree/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q

# Given the root of a binary tree, invert the tree, 
# and return its root.

# S

def levelOrderNodes(root, level):
    if root is None:
        return
        
    root.left , root.right = root.right, root.left
    levelOrderNodes(root.left, level+1)
    levelOrderNodes(root.right, level+1)

def levelOrder(root):
    levelOrderNodes(root, 0)

# def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
def invertTree(self, root):
    # if root:
    #     root.left , root.right = root.right, root.left
    
    # swap the left & right of the binary tree
    # use level order (BFS) to search from left to right
    # repeat until it's complete
    levelOrder(root)
    return root