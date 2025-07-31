# Linked List Cycle

# Given head, the head of a linked list, determine if the linked 
# list has a cycle in it.

# There is a cycle in a linked list if there is some node in the 
# list that can be reached again by continuously following 
# the next pointer. Internally, pos is used to denote 
# the index of the node that tail's next pointer is connected to. 

# Note that pos is not passed as a parameter.

# def hasCycle(self, head: Optional[ListNode]) -> bool:
def hasCycle(self, head):
    #floyd's hare & tortoise approach
    #set slow & fast pointers
    slow , fast = head , head

    #handle edge cases at start
    if fast is None or fast.next is None :
        return False            

    #loop until end or cycle found
    while(True):
        slow = slow.next
        #if there is a none , the no cycle exists
        if fast.next is None or fast.next.next is None:
            return False
        #else keep moving fast pointer by 2
        fast = fast.next.next

        # if slow & fast are at same point , cycle exists
        if slow == fast:
            return True