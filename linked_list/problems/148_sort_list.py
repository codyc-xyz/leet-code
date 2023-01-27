# Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []
        curr = head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            curr = curr.next
            i += 1
        return head

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        left = slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        tmp = slow.next
        slow.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
        
    def merge(self, left, right):
        dummy = tail = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next