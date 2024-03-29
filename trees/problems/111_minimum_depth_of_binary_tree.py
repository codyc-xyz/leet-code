# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.min = float('inf')

        def dfs(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.min = min(depth, self.min)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 1)
        return self.min

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            if not node.left:
                return dfs(node.right) + 1
            if not node.right:
                return dfs(node.left) + 1
            return min(dfs(node.left), dfs(node.right)) + 1
        return dfs(root)
    

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            depth += 1
            lenQ = len(q)
            for _ in range(lenQ):
                curr = q.popleft()
                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return depth