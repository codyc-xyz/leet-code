# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        curr = head
        length = 1
        while curr and curr.next:
            curr = curr.next
            length += 1
        tail = curr
        
        k = k % length
        if not k:
            return head
        
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        ans = curr.next
        curr.next = None
        tail.next = head
        return ans