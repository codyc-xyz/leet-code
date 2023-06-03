# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        def dfs(curr, target):
            if curr not in seen:
                seen.add(curr)

                if curr == target:
                    return True
                return any(dfs(n, target) for n in adj[curr])
            
        for e1, e2 in edges:
            seen = set()
            if e1 in adj and e2 in adj and dfs(e1, e2):
                return [e1, e2]
            adj[e1].append(e2)
            adj[e2].append(e1)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        rank = [1 for i in range(N + 1)]
        self.ans = 0
        def find(n):
            res = n
            while res != par[res]:
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                self.ans = [n1, n2]
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] += 1
      

        for e1, e2 in edges:
           union(e1, e2)
           if self.ans:
               return self.ans


            
