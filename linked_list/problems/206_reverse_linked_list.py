# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dq = deque()
        curr = head
        while curr:
            dq.append(curr.val)
            curr = curr.next
        ans = dummy = ListNode()   
        for i in range(len(dq) - 1, -1, -1):
            dummy.next = ListNode(dq[i])
            dummy = dummy.next
        return ans.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = None, head
        while r:
            nxt = r.next
            r.next = l
            l = r
            r = nxt
        return l