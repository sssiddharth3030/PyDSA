# Binary Search Tree

# left nodes should be smaller than root
# right nodes should be larger than root

import binaryTree

class node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def insert(root, data):
  if root is None:
    return node(data)
  
  if data < root.data:
    root.left = insert(root.left, data)
  elif data > root.data:
    root.right = insert(root.right, data)
    
  return root

def display(): #refer to in-order code in binary tree
  pass

def remove(root, data):
  # Base case
  if root is None:
    return None

  # If key to be searched is in a structure
  if data < root.data:
    root.left = remove(root.left, data)
  elif data > root.data:
    root.right = remove(root.right, data)
  else:
  # if root matches with the given key

    # Case 1: No child / Case 2: One child    
    # when only has right child
    if root.left is None:
      return root.right
    # when only has left child
    elif root.right is None:
      return root.left
    
    # Case 3: Two children
    # Find inorder successor (smallest in right subtree)
    temp = root.right
    while temp.left:
      temp = temp.left
    root.data = temp.data # Copy inorder successor's data to current node
    root.right = remove(root.right, temp.data)  # Delete inorder successor
  
  return root

def test_code():
  root = node(12)
  insert(root, 7)
  insert(root, 5)
  insert(root, 10)
  insert(root, 15)
  insert(root, 18)
  insert(root, 13)
  
  print( 'root: ', root.data )
  # print(root.left.data, root.data, root.right.data)
  print('\n')
  binaryTree.inOrder(root)

  remove(root, 15)
  print('\n')
  binaryTree.inOrder(root)
  
if __name__ == '__main__':
  test_code()