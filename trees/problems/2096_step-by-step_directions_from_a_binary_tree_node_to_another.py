# You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. 
# You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. 
# Each letter indicates a specific direction:

# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        parents = {}
        nodeParents = {}

        def dfs(root, parent):
            if not root:
                return
            if root.val == destValue:
                self.destination = root
            parents[root.val] = parent.val if parent else None
            nodeParents[root] = parent
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)

        start, dest = startValue, destValue
        seen = set()
    
        while start or dest:
            if start:
                if start in seen:
                    lca = start
                    break
                seen.add(start)
                start = parents[start]
            elif dest:
                if dest in seen:
                    lca = dest
                    break
                seen.add(dest)
                dest = parents[dest]
        ans = ""
        while startValue != lca:
            ans += 'U'
            startValue = parents[startValue]

        d = self.destination
        res = ""
        while d.val != lca:
            parent = nodeParents[d]
            if parent.left and parent.left == d:
                res = 'L' + res
            if parent.right and parent.right == d:
                res = 'R' + res
            d = parent

        return ans + res