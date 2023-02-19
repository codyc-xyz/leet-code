# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

# Note:

# The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
# A subtree of root is a tree consisting of root and all of its descendants.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        self.count = 0

        def dfs(root):
            if not root:
                return 0, 0
            lSum, lNodes = dfs(root.left)
            rSum, rNodes = dfs(root.right)
            s = lSum + rSum + root.val
            c = lNodes + rNodes + 1
            if s // c == root.val:
                self.count += 1
            return s, c
        dfs(root)
        return self.count