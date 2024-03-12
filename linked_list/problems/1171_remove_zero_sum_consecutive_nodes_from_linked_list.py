'''
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hm = {}
        currSum = 0
        curr = dummy = ListNode(next=head)

        while curr:
            currSum += curr.val
            hm[currSum] = curr
            curr = curr.next

        currSum = 0
        curr = dummy
        while curr:
            currSum += curr.val
            curr.next = hm[currSum].next
            curr = curr.next
        return dummy.next
