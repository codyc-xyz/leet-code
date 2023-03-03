# Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

# Note that the root node is at depth 1.

# The adding rule is:

# Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
# cur's original left subtree should be the left subtree of the new left subtree root.
# cur's original right subtree should be the right subtree of the new right subtree root.
# If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def dfs(root, depth, prev, bias):
            if depth == 1:
                if bias:
                    node = TreeNode(val, root)
                    prev.left = node
                    return node
                elif bias == False:
                    node = TreeNode(val, None, root)
                    prev.right = node
                    return node
                else:
                    node = TreeNode(val, root)
                    return node
            if not root:
                return 
            root.left = dfs(root.left, depth - 1, root, True)
            root.right = dfs(root.right, depth - 1, root, False)
            return root
        return dfs(root, depth, None, None)