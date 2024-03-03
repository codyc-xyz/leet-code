# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
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

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = ListNode(next=head), head
        dummy = l
        while r and n > 0:
            r = r.next
            n -= 1
        
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = curr = ListNode(next=head)
        i = 0
        while head:
            head = head.next
            i += 1
        k = i - n
        while k > 0:
            curr = curr.next
            k -= 1
        curr.next = curr.next.next
        return dummy.next
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = curr = ListNode(next=head)
        i = 0
        while head:
            head = head.next
            i+=1
        for _ in range(i-n):
            dummy = dummy.next
        dummy.next = dummy.next.next
        return curr.next