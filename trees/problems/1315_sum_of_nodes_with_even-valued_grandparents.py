# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

# A grandparent of a node is the parent of its parent if it exists.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        self.total = 0

        def dfs(root):
            if not root:
                return
            if not root.val % 2:
                if root.right:
                    if  root.right.right:
                        self.total += root.right.right.val
                    if root.right.left:
                        self.total += root.right.left.val
                if root.left:
                    if root.left.right:
                        self.total += root.left.right.val
                    if root.left.left:
                        self.total += root.left.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.total