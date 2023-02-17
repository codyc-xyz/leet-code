# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

# The test cases are generated so that the answer fits in a 32-bits integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [[root, str(root.val)]]

        while stack:
            node, val = stack.pop()

            if node.left:
                stack.append([node.left, val + str(node.left.val)])
            if node.right:
                stack.append([node.right, val + str(node.right.val)])
            if not node.left and not node.right:
                total += int(val, 2)
        return total

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def preorder(node, val):
            if not node:
                return
            preorder(node.left, val + str(node.val))
            preorder(node.right, val + str(node.val))
            if not node.left and not node.right:

                self.total += int(val + str(node.val), 2)
        preorder(root, '0')
        return self.total