# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        ans = dummy = TreeNode(root.val)

        def traverse(curr, dummy):
            if not curr:
                return 
            if curr.left:
                dummy.right = TreeNode(curr.left.val)
            if curr.right:
                dummy.left = TreeNode(curr.right.val)
            traverse(curr.left, dummy.right)
            traverse(curr.right, dummy.left)
        traverse(root, dummy)
        return ans

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
