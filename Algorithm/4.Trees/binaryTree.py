class node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
def inOrder(root):
  # left -> root -> right
  # is used in context of Binary Search Tree
  inOrder(root.left)
  print(root.data, ' ')
  inOrder(root.right)
  
def postOrder(root):
  # left -> right -> root
  # is used to delete a tree from leaf to root
  
  postOrder(root.left)
  postOrder(root.right)
  print(root.data, ' ')
  
def preOrder(root):
  # root -> left -> right
  # is used to copy a tree from root to leaf
  
  print(root.data, ' ')
  preOrder(root.left)
  preOrder(root.right)
  
