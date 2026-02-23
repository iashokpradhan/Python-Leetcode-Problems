# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Edge cases: empty list or single node
        if not head or not head.next:
            return head
            
        # odd points to the start of odd-indexed nodes
        # even points to the start of even-indexed nodes
        odd = head
        even = head.next
        
        # even_head remembers the beginning of even list (needed at the end)
        even_head = even
        
        # Traverse and rearrange
        while even and even.next:
            # Connect next odd node
            odd.next = even.next
            odd = odd.next
            
            # Connect next even node
            even.next = odd.next
            even = even.next
        
        # Connect the end of odd list to start of even list
        odd.next = even_head
        
        return head