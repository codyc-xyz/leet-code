# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder(root):
            if not root:
                return 
            res.append('(')
            res.append(str(root.val))

            if not root.left and root.right:
                res.append('()')
            preorder(root.left)
            preorder(root.right)
            res.append(')')
        preorder(root)
        return "".join(res)[1:-1]

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""

        string = str(root.val)
        if not root.left and not root.right:
            return string
        if not root.left:
            string = string + '()' + '(' + self.tree2str(root.right) + ')'
        elif not root.right:
            string = string + '(' + self.tree2str(root.left) + ')'
        else:
            string = string + '(' + self.tree2str(root.left) + ')' + '(' + self.tree2str(root.right) + ')'
        return string

