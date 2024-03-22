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

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt  
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        firstHalf = []
        secondHalf = []
        while slow:
            firstHalf.append(head.val)
            secondHalf.append(slow.val)
            head = head.next
            slow = slow.next

        return firstHalf == secondHalf[::-1]