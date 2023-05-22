# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = defaultdict(list)

        for e1, e2 in edges:
            heapq.heappush(adj[e1], e2)
            heapq.heappush(adj[e2], e1)

        curr = [source]
        while curr:
            currNode = heapq.heappop(curr)
            if currNode == destination:
                return True
            while adj[currNode]:
                heapq.heappush(curr, heapq.heappop(adj[currNode]))

        return False

        