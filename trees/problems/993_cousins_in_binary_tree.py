# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        self.xDepth, self.xParent = 0, None
        self.yDepth, self.yParent = 0, None

        def dfs(root, depth, prev=None):
            if not root:
                return
            if root.val == x:
                self.xDepth = depth
                self.xParent = prev
            elif root.val == y:
                self.yDepth = depth
                self.yParent = prev
            dfs(root.left, depth + 1, prev=root.val)
            dfs(root.right, depth + 1, prev=root.val)
        dfs(root, 0)
        return (self.xDepth == self.yDepth) and (self.xParent != self.yParent)