# Given a binary tree root and a linked list with head as the first node. 

# Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
# In this context downward path means a path that starts at some node and goes downwards.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        target = []
        while head:
            target.append(head.val)
            head = head.next
        n = len(target)
        
        def dfs(root, path):
            if not root:
                return False
            path.append(root.val)
            if path == target or path[len(path) - n:] == target:
                return True
            l = dfs(root.left, path[:])
            r = dfs(root.right, path[:])
            return l or r
        return dfs(root, [])