class node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
def inOrder(root):
  # left -> root -> right
  # is used in context of Binary Search Tree
  if root is None:
    return
  inOrder(root.left)
  print(root.data, end=" ")
  inOrder(root.right)
  
def postOrder(root):
  # left -> right -> root
  # is used to delete a tree from leaf to root
  if root is None:
    return
  postOrder(root.left)
  postOrder(root.right)
  print(root.data, end=" ")
  
def preOrder(root):
  # root -> left -> right
  # is used to copy a tree from root to leaf
  if root is None:
    return  
  print(root.data, end=" ")
  preOrder(root.left)
  preOrder(root.right)
  
