# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dq = deque()
        curr = fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        while slow:
            dq.append(slow.val)
            slow = slow.next
        while dq:
            if dq.pop() != curr.val:
                return False
            curr = curr.next
        return True