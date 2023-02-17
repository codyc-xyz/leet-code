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
        def traverse(root, k):
            if not root:
                return False
            if k - root.val in seen:
                return True
            seen.add(root.val)
            return traverse(root.left, k) or traverse(root.right, k)
        return traverse(root, k)