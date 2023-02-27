# Given the root of a binary tree, the depth of each node is the shortest distance to the root.

# Return the smallest subtree such that it contains all the deepest nodes in the original tree.

# A node is called the deepest if it has the largest depth possible among any node in the entire tree.

# The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return None, 0
            l = dfs(root.left)
            r = dfs(root.right)
            if l[1] > r[1]:
                return l[0], l[1] + 1
            if r[1] > l[1]:
                return r[0], r[1] + 1
            else:
                return root, l[1] + 1
        return dfs(root)[0]