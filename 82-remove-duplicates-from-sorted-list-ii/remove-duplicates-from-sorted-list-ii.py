class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next:
            # If this value appears at least twice
            if prev.next.next and prev.next.val == prev.next.next.val:
                val = prev.next.val
                # Skip ALL nodes with this value
                while prev.next and prev.next.val == val:
                    prev.next = prev.next.next
            else:
                prev = prev.next
                
        return dummy.next