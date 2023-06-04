# There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

# You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

# Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        N = len(connections)

        if N < n - 1:
            return -1

        adj = defaultdict(list)

        for n1, n2 in connections:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(n):
            if n in seen:
                return 0
            seen.add(n)
            for nei in adj[n]:
                if nei not in seen:
                    dfs(nei)
            return 1

        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                ans += dfs(i)

        return ans - 1
