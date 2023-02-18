# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        seen = set()
        self.min = float('inf')
        def dfs(root):
            if not root:
                return
            for v in seen:
                if abs(v - root.val) < self.min:
                    self.min = abs(v - root.val)
            seen.add(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.min