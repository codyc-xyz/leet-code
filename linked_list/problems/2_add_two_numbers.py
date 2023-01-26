# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = l1, l2
        nums1, nums2 = "", ""
        while curr1:
            nums1 = str(curr1.val) + nums1
            curr1 = curr1.next
        
        while curr2:
            nums2 = str(curr2.val) + nums2
            curr2 = curr2.next
      
        res = str(int(nums1) + int(nums2))
        dummy = head = ListNode()
        for c in res[::-1]:
            dummy.next = ListNode(int(c))
            dummy = dummy.next
        return head.next