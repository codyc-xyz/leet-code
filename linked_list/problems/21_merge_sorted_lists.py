# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = dummy = ListNode()
        l1, l2 = list1, list2
        while l1 and l2:
            if l1 and l1.val < l2.val:
                dummy.next = ListNode(l1.val)
                l1 = l1.next
            else:
                dummy.next = ListNode(l2.val)
                l2 = l2.next
            dummy = dummy.next
        while l1:
            dummy.next = ListNode(l1.val)
            l1 = l1.next
            dummy = dummy.next
        while l2:
            dummy.next = ListNode(l2.val)
            l2 = l2.next
            dummy = dummy.next
        return ans.next