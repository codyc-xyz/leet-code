# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.val = 0
        def dfs(root):
            if not root:
                return 
            if low <= root.val <= high:
                self.val += root.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.val