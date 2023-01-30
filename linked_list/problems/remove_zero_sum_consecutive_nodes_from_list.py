# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

# After doing so, return the head of the final linked list.  You may return any such answer.

# (Note that in the examples below, all sequences are serializations of ListNode objects.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode(0, next = head)
        hm = {}
        currSum = 0
        remove = []
        while curr:
            currSum += curr.val
            hm[currSum] = curr
            curr = curr.next
        
        curr = dummy
        currSum = 0
        while curr:
            currSum += curr.val
            curr.next = hm[currSum].next
            curr = curr.next
           
        return dummy.next