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
            