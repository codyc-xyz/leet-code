# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
  
        ans = slow = fast = head
        while fast:
            if slow.val == fast.val:
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        return ans
            