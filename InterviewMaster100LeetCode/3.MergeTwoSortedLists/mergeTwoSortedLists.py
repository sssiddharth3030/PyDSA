#  https://leetcode.com/problems/merge-two-sorted-lists/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

# Q 

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

def mergeTwoLists(self, list1, list2):
    head = ListNode()
    tail = head

    # when both list are not empty
    while list1 is not None and list2 is not None:
        # if value of list is smaller , add list1 to tail & iterate list 1
        # else add list 2 to tail & iterate list 2
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
            tail = tail.next

    # if either list is Null & the other is not null
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    # return the mergered list
    return head.next