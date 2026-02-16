# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        # Two pointers starting at heads
        a = headA
        b = headB
        
        # Traverse until they meet (or both become None)
        while a != b:
            # When a reaches end of list A → jump to headB
            a = a.next if a else headB
            # When b reaches end of list B → jump to headA
            b = b.next if b else headA
        
        # If they meet at a node → that's the intersection
        # If they meet at None → no intersection
        return a