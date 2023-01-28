# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans = front = ListNode()
        curr = head
        dummy = rev = ListNode()
        length = 1
        while curr and length <= right:
            if right >= length >= left:
                rev.next = curr
                rev = rev.next
            elif length < left:
                front.next = curr
                front = front.next
            length += 1
            curr = curr.next
        tail = curr
        rev.next = None
        
        res = curr = dummy.next
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        front.next = prev
        res.next = tail
        
        return ans.next