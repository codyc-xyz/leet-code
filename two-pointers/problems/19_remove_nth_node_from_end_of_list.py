# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = slow = head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return head