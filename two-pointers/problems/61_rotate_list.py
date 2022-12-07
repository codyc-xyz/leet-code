# Given the head of a linked list, rotate the list to the right by k places.

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 0 or not head:
            return head
        arr = []
        length = head
        i = 0
        while length:
            arr.append(length.val)
            length = length.next
            i += 1
        
        rotations = k % i
        start = i - rotations
        curr = head
        while start < i:
            curr.val = arr[start]
            curr = curr.next
            start += 1
        
        j = 0
        while curr:
            curr.val = arr[j]
            curr = curr.next
            j += 1
        return head

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        i, tail = 1, head
        
        while tail.next:
            tail = tail.next
            i += 1
            
        k = k % i
        
        if k == 0:
            return head
        
        curr, j = head, 0
        
        while j < i - k - 1:
            curr = curr.next
            j += 1
        
        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead
            