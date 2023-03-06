# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        inorder = []

        def dfs(root):
            if not root:
               return
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
            
        dfs(root)
        inorder.sort()
        self.i = 0

        def dfs2(root):
            if not root:
                return
            dfs2(root.left)
            root.val = inorder[self.i]
            self.i += 1
            dfs2(root.right)
        dfs2(root)
        return root