# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        N = len(points)
        adj = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
               x2, y2 = points[j]
               dist = abs(x1 - x2) + abs(y1 - y2)
               heapq.heappush(adj[i], (dist, j))
               heapq.heappush(adj[j], (dist, i))

        ans = 0
        seen = set()

        heap = [[0, 0]]

        while len(seen) < N:
            cost, i = heapq.heappop(heap)
            if i in seen:
                continue
            ans += cost
            seen.add(i)
            for nCost, n in adj[i]:
                if n not in seen:
                    heapq.heappush(heap, ((nCost, n)))
        return ans
