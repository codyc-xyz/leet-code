# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        self.seen = set()
        def dfs(node):
            if not node:
                return 
            self.seen.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return len(self.seen) == 1

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        stack = [[root, root.val]]
        while stack:
            node, val = stack.pop()
            if node.left:
                if val != node.left.val:
                    return False
                else:
                    stack.append([node.left, node.left.val])
            if node.right:
                if val != node.right.val:
                    return False
                else:
                    stack.append([node.right, node.right.val])
        return True