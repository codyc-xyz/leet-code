# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = odds = ListNode()
        dummy = evens = ListNode()
        curr = head
        i = 1
        while curr:
            if i % 2:
                odds.next = curr
                odds = odds.next
            else:
                evens.next = curr
                evens = evens.next
            curr = curr.next
            i += 1
        
        evens.next = None
        odds.next = dummy.next
        return ans.next