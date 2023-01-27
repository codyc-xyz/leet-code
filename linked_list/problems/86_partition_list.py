# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        curr = head
        dummy = ans = ListNode()
        while curr:
            if curr.val < x:
                dummy.next = ListNode(curr.val)
                dummy = dummy.next
            curr = curr.next
        curr = head
        
        while curr:
            if curr.val >= x:
                dummy.next = ListNode(curr.val)
                dummy = dummy.next
            curr = curr.next
        return ans.next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        curr = head
        dummyL = left = ListNode()
        dummyR = right = ListNode()
        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            curr = curr.next
        left.next = dummyR.next
        right.next = None
        return dummyL.next