# You are given the head of a linked list.

# Remove every node which has a node with a strictly greater value anywhere to the right side of it.

# Return the head of the modified linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = deque()
        tmp = head
        while tmp:
            while stack and tmp.val > stack[-1].val:
                stack.pop()
            stack.append(tmp)
            tmp = tmp.next
        
        dummy = ans = ListNode(0)
        
        while stack:
            dummy.next = stack.popleft()
            dummy = dummy.next
        return ans.next
        