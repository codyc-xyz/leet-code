# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        dq = deque()
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        while slow:
            dq.appendleft(slow.val)
            slow = slow.next

        for i in range(len(dq)):
            if dq[i] != head.val:
                return False
            head = head.next
        return True