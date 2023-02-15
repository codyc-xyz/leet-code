# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.flag = False
        currSum = 0
        def dfs(root, currSum):
            if not root:
                return
            currSum += root.val
            dfs(root.left, currSum)
            dfs(root.right, currSum)
            if not root.left and not root.right and currSum == targetSum:
                self.flag = True
        dfs(root, currSum)
        return self.flag 
