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
        length = 0
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
            length += 1
        
        k = k % length
        if not k:
            return head
        
        start = length - k
        curr = head
        while start < length:
            curr.val = arr[start]
            start += 1
            curr = curr.next
            
        i = 0
        while curr:
            curr.val = arr[i]
            curr = curr.next
            i += 1
            
        return head