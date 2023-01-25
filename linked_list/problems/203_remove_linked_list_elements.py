# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        curr = head
        dq = deque()
        while curr:
            if curr.val != val:
                dq.append(curr.val)
            curr = curr.next
        
        ans = dummy = ListNode()
        
        for v in dq:
            dummy.next = ListNode(v)
            dummy = dummy.next
        return ans.next