# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

# Note that you need to maximize the answer before taking the mod and not after taking it.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        mod = 10**9+7
        self.maxSum = float('-inf')
        self.treeSum = 0
        def findTreeSum(root):
            if not root:
                return
            self.treeSum += root.val
            findTreeSum(root.left)
            findTreeSum(root.right)
        findTreeSum(root)

        def dfs(root):
            if not root:
                return 0
           
            l = dfs(root.left)
            r = dfs(root.right)
            rootSum = l + r + root.val
            if (self.treeSum - r) * r > self.maxSum:
                self.maxSum = (self.treeSum - r) * r
            if (self.treeSum - l) * l > self.maxSum:
                self.maxSum = (self.treeSum - l) * l
            return rootSum
        dfs(root)
        return self.maxSum%mod