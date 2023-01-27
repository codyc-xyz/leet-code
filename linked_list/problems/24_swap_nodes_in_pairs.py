# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ans = ListNode(next=head)
        
        while dummy and dummy.next and dummy.next.next:
            a = dummy.next
            b = dummy.next.next
            dummy.next, a.next, b.next = b, b.next, a
            dummy = a
        return ans.next