# You are given two linked lists: list1 and list2 of sizes n and m respectively.

# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

# The blue edges and nodes in the following figure indicate the result:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(next=list1)
        i = 1
        while i < a:
            list1 = list1.next
            i += 1
        tail = list1.next
        list1.next = list2
        
        while i <= b:
            tail = tail.next
            i += 1
            
        curr = list2
        while curr and curr.next:
            curr = curr.next
        
        curr.next = tail
        return dummy.next
        
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail = curr = dummy = ListNode(next=list1)
        
        head = ListNode(next=list2)
        while b >= -1:
            tail = tail.next
            b -= 1

        length = 0
        while curr:
            if length == a:
                curr.next = head.next
                while curr.next:
                    curr = curr.next
                curr.next = tail
                break
            curr = curr.next
            length += 1
        return dummy.next

