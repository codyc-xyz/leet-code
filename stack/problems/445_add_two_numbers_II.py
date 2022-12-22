# You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        c1, c2 = l1, l2
        l1, l2 = deque(), deque()
        while c1:
            l1.append(c1.val)
            c1 = c1.next
        
        while c2:
            l2.append(c2.val)
            c2 = c2.next
            
        p1 = len(l1) - 1
        p2 = len(l2) - 1
        ans = deque()
        carry = 0
        while p1 >= 0 and p2 >= 0:
            res = carry + l1[p1] + l2[p2] 
            if res > 9:
                res = str(res)
                a,b = res[0], res[1]
                ans.appendleft(int(b))
                carry = int(a)
            else:
                ans.appendleft(res)
                carry = 0
            p1 -= 1
            p2 -= 1
        
        while p1 >= 0:
            res = l1[p1] + carry
            if res > 9:
                res = str(res)
                a,b = res[0], res[1]
                ans.appendleft(int(b))
                carry = int(a)
            else:
                ans.appendleft(res)
                carry = 0
            p1 -= 1
        
        while p2 >= 0:
            res = l2[p2] + carry
            if res > 9:
                res = str(res)
                a,b = res[0], res[1]
                ans.appendleft(int(b))
                carry = int(a)
            else:
                ans.appendleft(res)
                carry = 0
            p2 -= 1
        if carry:
            ans.appendleft(carry)
            
        dummy = final = ListNode()
        
        while ans:
            dummy.next = ListNode(ans.popleft())
            dummy = dummy.next
        return final.next