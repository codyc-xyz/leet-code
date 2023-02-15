# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxCount = 0

        def traverse(root, count):
            if not root:
                return
            traverse(root.left, count + 1)
            traverse(root.right, count + 1)
            self.maxCount = max(count, self.maxCount)
        
        traverse(root, 1)
        return self.maxCount