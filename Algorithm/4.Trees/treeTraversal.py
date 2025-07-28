import binaryTree

root = None

if __name__ == '__main__':

  # structure of below Tree  
    #     1
    #    / \
    #   2   3
    #  / \  /
    # 4  5 6
    
  # Expected Results :
  # In Order: 
  # 4 2 5 1 6 3 

  # Post Order: 
  # 4 5 2 6 3 1 

  # Pre Order: 
  # 1 2 4 5 3 6 

  root = binaryTree.node(1)
  root.left = binaryTree.node(2)
  root.right = binaryTree.node(3)
  root.left.left = binaryTree.node(4)
  root.left.right = binaryTree.node(5)
  root.right.left = binaryTree.node(6)
  
  print('In Order: ')
  binaryTree.inOrder(root) # left -> root -> right #for BST traversal
  print('\n')
  print('Post Order: ')
  binaryTree.postOrder(root) # left -> right -> root #for deleting
  print('\n')
  print('Pre Order: ')
  binaryTree.preOrder(root) # root -> left -> right #for cloning
  print('\n')