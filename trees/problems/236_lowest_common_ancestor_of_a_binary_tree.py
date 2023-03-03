# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parents = {}

        def dfs(root, prev):
            if not root:
                return
            parents[root] = prev
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)
        
        seen = set()
        while p or q:
            if p:
                if p in seen:
                    return p
                seen.add(p)
                p = parents[p]
            if q:
                if q in seen:
                    return q
                seen.add(q)
                q = parents[q]
        return root
