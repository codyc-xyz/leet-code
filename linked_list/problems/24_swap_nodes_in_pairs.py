# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        ans = dummy = ListNode(next=head)

        while dummy and dummy.next and dummy.next.next:
            fast = dummy.next.next
            slow = dummy.next

            dummy.next, slow.next, fast.next = fast, fast.next, slow

            dummy = slow
        return ans.next