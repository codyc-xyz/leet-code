# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

# Each minute, a node becomes infected if:

# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        nodes = {}
        seen = set()
        def dfs(root, prev):
            if not root:
                return
            parent[root] = prev
            nodes[root.val] = root
            seen.add(root)
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)

        visited = set()
        self.count = 0
        self.maxDepth = 0
        self.flag = False
        def dfs(curr, depth):
            if not curr or self.flag == True:
                return
            self.maxDepth = max(depth, self.maxDepth) 
            visited.add(curr)
            if len(visited) == len(seen):
                self.count = self.maxDepth
                self.flag = True
                return

            for n in (curr.left, curr.right, parent[curr]):
                if n and n not in visited:
                    dfs(n, depth + 1)
            
        dfs(nodes[start], 0)
        return self.count 
    

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        nodes = {}
        seen = set()

        def dfs(root, prev):
            if not root:
                return
            parent[root] = prev
            nodes[root.val] = root
            seen.add(root)
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)

        visited = set()
        self.count = 0
        self.maxDepth = 0
        self.flag = False

        def dfs(curr, depth):
            if not curr or self.flag == True:
                return
            self.maxDepth = max(depth, self.maxDepth)
            visited.add(curr)
            if len(visited) == len(seen):
                self.count = self.maxDepth
                self.flag = True
                return

            for n in (curr.left, curr.right, parent[curr]):
                if n and n not in visited:
                    dfs(n, depth + 1)

        dfs(nodes[start], 0)
        return self.count
