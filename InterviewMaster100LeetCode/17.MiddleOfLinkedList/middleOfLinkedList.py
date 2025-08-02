# https://leetcode.com/problems/middle-of-the-linked-list/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q
# Given the head of a singly linked list, return the 
# middle node of the linked list.

# If there are two middle nodes, return the second middle node. 

# S

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
        
class Solution:
  # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
  def middleNode(self, head):
    # set two pointers at head
    slow , fast = head, head
    # if next is None, break the loop
    # if next.next is None , iterate slow to set 2nd middle
    # return the slow pointer
    while fast:
      if fast.next is None:
        break
      elif fast.next.next is None:
        slow = slow.next
        break
            
      slow = slow.next
      fast = fast.next.next

    return slow