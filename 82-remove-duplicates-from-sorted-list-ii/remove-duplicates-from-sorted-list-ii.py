# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list or single node
        if not head or not head.next:
            return head
        
        # Use a dummy node to handle cases where head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # If we found duplicate values
            if prev.next.val == prev.next.next.val:
                # Skip all nodes with this value
                duplicate_val = prev.next.val
                while prev.next and prev.next.val == duplicate_val:
                    prev.next = prev.next.next
            else:
                # No duplicate → move forward
                prev = prev.next
        
        return dummy.next