# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        seen = set()
        self.flag = False
        def traverse(root, k):
            if not root:
                return
            if k - root.val in seen:
                self.flag = True
            seen.add(root.val)
            traverse(root.left, k)
            traverse(root.right, k)
        traverse(root, k)
        return self.flag