# You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

# You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

# Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

# A node u is an ancestor of another node v if u can reach v via a set of edges.

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        adj = defaultdict(list)

        for e1, e2 in edges:
            adj[e1].append(e2)


        def dfs(curr, path):
            for p in path:
                if p not in ans[curr]:
                    ans[curr].append(p)
            path.append(curr)
            for n in adj[curr]:
                if n not in path:
                    dfs(n, path[:])

            
        ans = [[] for _ in range(n)]
        for i in range(n):
            dfs(i, [])

        for anc in ans:
            anc.sort()
        return ans