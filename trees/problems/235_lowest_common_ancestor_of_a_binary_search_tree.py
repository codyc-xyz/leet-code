# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        hm = {}

        def dfs(root, parent, depth):
            if not root:
                return
            hm[root] = (parent, depth)
            dfs(root.left, root, depth + 1)
            dfs(root.right, root, depth + 1)
        dfs(root, root, 1)
        first, second = hm[p], hm[q]
        
        if p == second:
            return p
        elif q == first:
            return q
        seen = set()
        ancestors = set()
        seen.add(p)
        seen.add(q)
        
        while first[0] != second[0]:
            if first[0] in seen:
                ancestors.add(first[0])
            else:
                seen.add(first[0])
            if second[0] in seen:
                ancestors.add(second[0])
            else:
                seen.add(second[0])
            first = hm[first[0]]
            second = hm[second[0]]

        ancestors.add(first[0])
        ans = root
        maxDepth = 1
        for node in ancestors:
            if hm[node][1] > maxDepth:
                ans = node
                maxDepth = hm[node][1]
        return ans
