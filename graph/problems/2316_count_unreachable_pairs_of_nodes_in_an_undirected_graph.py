# You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

# Return the number of pairs of different nodes that are unreachable from each other.

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
       

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        seen = set()
        sizes = []
        def dfs(curr):
            size = 1
            seen.add(curr)

            for n in adj[curr]:
                if n not in seen:
                    size += dfs(n)
            return size

        for i in range(n):
            if i not in seen:
                sizes.append(dfs(i))

        remaining = sum(sizes)
        ans = 0
        for i in range(len(sizes)):
            remaining -= sizes[i]
            ans += sizes[i] * remaining
        return ans
