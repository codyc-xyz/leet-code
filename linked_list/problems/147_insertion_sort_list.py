# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:
# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(next=head)

        prev, curr = head, head.next

        while curr:
            if curr.val >= prev.val:
                prev, curr = curr, curr.next
                continue
            tmp = dummy

            while curr.val > tmp.next.val:
                tmp = tmp.next
            
            prev.next = curr.next
            curr.next = tmp.next
            tmp.next = curr
            curr = prev.next
        return dummy.next