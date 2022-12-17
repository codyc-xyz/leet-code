# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        dq = deque()
        while curr:
            dq.append(curr.val)
            curr = curr.next
        
        while dq:
            if head.val != dq.pop():
                return False
            head = head.next
        return True