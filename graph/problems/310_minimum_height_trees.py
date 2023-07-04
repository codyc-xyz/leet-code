# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

class Solution:
    def findMinHeightTrees(self, N: int, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        def dfs(curr, depth):
            seen.add(curr)
            for n in adj[curr]:
                if n not in seen:
                    dfs(n, depth + 1)

            self.maxDepth = max(self.maxDepth, depth)
        hm = {}
        for i in range(N):
            seen = set()
            self.maxDepth = 0
            dfs(i, 0)
            if self.maxDepth in hm:
                hm[self.maxDepth].append(i)
            else:
                hm[self.maxDepth] = [i]

        return hm[min(hm)]

class Solution:
    def findMinHeightTrees(self, N: int, edges: List[List[int]]) -> List[int]:
        if N == 1:
            return [0]
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        leaves = [n for n in adj if len(adj[n]) == 1]

        while N > 2:
            N -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                nei = adj[leaf].pop()
                adj[nei].remove(leaf)
                if len(adj[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves

        return leaves
