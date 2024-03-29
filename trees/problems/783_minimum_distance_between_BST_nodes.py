# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        vals = []
        def inorder(root, prev=None):
            if not root:
                return
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)
        inorder(root)

        ans = float('inf')
        for i in range(1, len(vals)):
            if vals[i] - vals[i - 1] < ans:
                ans = vals[i] - vals[i - 1]
        return ans