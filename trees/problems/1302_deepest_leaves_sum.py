# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        levels = defaultdict(int)
        def dfs(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                levels[depth] += root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 1)
        return levels[max(levels, key=int)]