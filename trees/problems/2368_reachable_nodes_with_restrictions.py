# There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

# Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

# Note that node 0 will not be a restricted node.

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        nodes = defaultdict(list)
        nodes[0].append(None)
        for e1, e2 in edges:
            if e1 not in restricted and e2 not in restricted:
                nodes[e1].append(e2)
                nodes[e2].append(e1)

        visited = set()
        def dfs(n):
            if not nodes[n]:
                return 
            visited.add(n)
            for c in nodes[n]:
                if c not in visited:
                    dfs(c)
        dfs(0)
        return len(visited)