# You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

# The score of a path between two cities is defined as the minimum distance of a road in this path.

# Return the minimum possible score of a path between cities 1 and n.

# Note:

# A path is a sequence of roads between two cities.
# It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
# The test cases are generated such that there is at least one path between 1 and n.

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adj = defaultdict(list)

        for r1, r2, cost in roads:
            heapq.heappush(adj[r1], (cost, r2))
            heapq.heappush(adj[r2], (cost, r1))

        self.ans = float('inf')
        def dfs(curr, target):
            while adj[curr]:
                cost, node = heapq.heappop(adj[curr])
                self.ans = min(self.ans, cost)
                dfs(node, target)

        dfs(1, n)
        return self.ans if self.ans != float('inf') else 0

