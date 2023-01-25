# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i = 0
        l1, l2 = headA, headB
        while i < 3:
            flag1 = flag2 = False
            if l1 == l2:
                return l1
            if not l1.next:
                l1 = headB
                i += 1
                flag1 = True
            if not l2.next:
                l2 = headA
                i += 1
                flag2 = True
            if flag1 == False:
                l1 = l1.next
            if flag2 == False:
                l2 = l2.next
        return None