# Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []
        curr = head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            curr = curr.next
            i += 1
        return head