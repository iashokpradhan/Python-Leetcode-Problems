# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find length and the current tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Connect tail to head → make it circular
        tail.next = head
        
        # Step 3: Effective rotations (k can be >> length)
        k = k % length
        
        # If k becomes 0 after modulo → no rotation needed
        if k == 0:
            tail.next = None
            return head
        
        # Step 4: Move (length - k - 1) steps from head to find new tail
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # New head is the node after new_tail
        new_head = new_tail.next
        
        # Break the circle
        new_tail.next = None
        
        return new_head