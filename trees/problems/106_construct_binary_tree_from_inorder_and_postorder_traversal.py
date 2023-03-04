# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(inorder, postorder):
            if not inorder or not postorder:
                return
            root = TreeNode(postorder[-1])
            m = inorder.index(postorder[-1])
            root.left = dfs(inorder[:m], postorder[:m])
            root.right = dfs(inorder[m + 1:], postorder[m:-1])
            return root
        return dfs(inorder, postorder)