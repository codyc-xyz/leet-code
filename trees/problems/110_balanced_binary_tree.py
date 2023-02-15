# Given a binary tree, determine if it is height-balanced

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True

        def traverse(root):
            if not root:
                return 0
            l = traverse(root.left)
            r = traverse(root.right)
            res = abs(l) - abs(r)
            if res > 1 or res < -1:
                self.flag = False
            return max(l, r) + 1
        traverse(root)
        return self.flag