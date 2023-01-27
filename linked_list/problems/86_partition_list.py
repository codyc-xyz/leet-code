# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        arr = []
        curr = head
        while curr:
            if curr.val < x:
                arr.append(curr.val)
            curr = curr.next
        curr = head
        
        while curr:
            if curr.val >= x:
                arr.append(curr.val)
            curr = curr.next
        dummy = ans = ListNode()
        
        for i in range(len(arr)):
            dummy.next = ListNode(arr[i])
            dummy = dummy.next
        return ans.next