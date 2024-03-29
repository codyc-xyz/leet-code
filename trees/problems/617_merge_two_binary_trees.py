# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. 
# You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def merge(root1, root2):
            if root1 and root2:
                node = TreeNode(root1.val + root2.val)
            elif root1:
                node = TreeNode(root1.val)
            elif root2:
                node = TreeNode(root2.val)
            else:
                return None
            node.left = merge(root1.left if root1 else None, root2.left if root2 else None)
            node.right = merge(root1.right if root1 else None, root2.right if root2 else None)
            return node
        return merge(root1, root2)

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
        elif root1:
            node = TreeNode(root1.val)
        else:
            node = TreeNode(root2.val)
        node.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        node.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return node