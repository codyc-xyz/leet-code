# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        tail, length = head, 1

        while tail and tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        kth = self.findKth(head, k, length)

        ans = kth.next
        kth.next = None
        tail.next = head
        return ans

    def findKth(self, curr, k, length):
        for i in range(length - k - 1):
            curr = curr.next

        return curr