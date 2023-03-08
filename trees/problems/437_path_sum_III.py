# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int: 
        self.count = 0
        def sumNodes(node, curr):
            if not node:
                return
            sumNodes(node.left, curr + node.val)
            sumNodes(node.right, curr + node.val)
            if curr + node.val == targetSum:
                self.count += 1

        def dfs(root):
            if not root:
                return 
            sumNodes(root, 0)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.count