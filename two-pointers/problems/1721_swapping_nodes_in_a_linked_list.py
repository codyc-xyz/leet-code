# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        curr = head
        
        dq = deque()
        while curr:
            dq.append(curr.val)
            curr = curr.next
        
        tmp = dq[k - 1]
        dq[k - 1] = dq[-k]
        dq[-k] = tmp
        
        alt = dummy = ListNode()
        for i in dq:
            alt.next = ListNode(i)
            alt = alt.next
        return dummy.next