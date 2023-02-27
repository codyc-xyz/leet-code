# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

# Recall that:

# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
# The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def postorder(root):
            if not root:
                return None, 0
            l = postorder(root.left)
            r = postorder(root.right)
            if l[1] > r[1]:
                return l[0], l[1] + 1
            elif r[1] > l[1]:
                return r[0], r[1] + 1
            else:
                return root, l[1] + 1
        return postorder(root)[0]