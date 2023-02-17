# Given the root of a binary tree, return the sum of every tree node's tilt.

# The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(root):
            if not root:
                 return 0
            l = dfs(root.left)
            r = dfs(root.right)
            tilt = abs(l - r)
            self.total += tilt
            return l + r + root.val
        dfs(root)
        return self.total