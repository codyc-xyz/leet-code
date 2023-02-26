# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

# If there exist multiple answers, you can return any of them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        idx = postorder.index(preorder[1])

        root.left = self.constructFromPrePost(preorder[1:idx + 2], postorder[:idx + 1])
        root.right = self.constructFromPrePost(preorder[idx + 2:], postorder[idx + 1:])
        return root

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        stack = [TreeNode(preorder[0])]

        j = 0

        for v in preorder[1:]:
            node = TreeNode(v)
            while stack[-1].val == postorder[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]