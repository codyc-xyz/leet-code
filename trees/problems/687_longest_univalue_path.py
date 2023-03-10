# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.maxUni = 0
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            if root.left and root.left.val == root.val:
                l += 1
            else:
                l = 0
            r = dfs(root.right)
            if root.right and root.right.val == root.val:
                r += 1
            else: 
                r = 0
            self.maxUni = max(self.maxUni, l + r)
            return max(l, r)
        dfs(root)
        return self.maxUni