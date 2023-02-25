# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxDiff = 0

        def dfs(root, minVal, maxVal):
            if not root:
                return
            
            if root.val < minVal: minVal = root.val
            if root.val > maxVal: maxVal = root.val
            self.maxDiff = max(self.maxDiff, maxVal - minVal)
            dfs(root.left, minVal, maxVal)
            dfs(root.right, minVal, maxVal)

        dfs(root, float('inf'), float('-inf'))
        return self.maxDiff