# https://leetcode.com/problems/reverse-linked-list/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Given the head of a singly linked list, 
# reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# singly list , reverse the list
# watch neet code, for better explanation: https://www.youtube.com/watch?v=G0_I-ZF0S38

class Solution:
  # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  def reverseList(self, head):
    prev, curr = None,  head

    while curr:
      nxt = curr.next
      curr.next = prev
      prev = curr
      curr = nxt

    return prev