# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node, path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append("->".join(path))
                path.pop()
                return
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return ans