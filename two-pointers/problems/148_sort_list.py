# Given the head of a linked list, return the list after sorting it in ascending order.

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dq = deque()
        curr = head
        while curr:
            dq.append(curr.val)
            curr = curr.next
        sortDq = sorted(dq)
        
        sort = head
        while sort:
            sort.val = sortDq.pop(0)
            sort = sort.next
        return head