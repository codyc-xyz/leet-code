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

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count = head
        n = 0
        while count:
            n += 1
            count = count.next
        
        right = head
        end_node = n - k
        while end_node > 0:
            right = right.next
            end_node -= 1
        
        left = head
        start_node = k - 1
        while start_node > 0:
            left = left.next
            start_node -= 1
            
        tmp = right.val
        right.val = left.val
        left.val = tmp
        return head