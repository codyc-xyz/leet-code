# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = prevL = ListNode(next=head)
        curr = head
        
        for i in range(left - 1):
            prevL, curr = curr, curr.next
            
        prev = None
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        prevL.next.next = curr
        prevL.next = prev
        
        return dummy.next
    

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        curr = head
        prev = None

        for i in range(left - 1):
            prev = curr
            curr = curr.next

        con, tail = prev, curr
        remainder = right - left

        while remainder >= 0:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            remainder -= 1

        if con:
            con.next = prev
        # If 'con' is None, it means the reversed segment starts from the head. Update the head.
        else:
            head = prev

        # 'tail' is the end of the reversed segment. Link it to 'curr', which is the node after the reversed segment
        tail.next = curr

        # Return the modified list
        return head
