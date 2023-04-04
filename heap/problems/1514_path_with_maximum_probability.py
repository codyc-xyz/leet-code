# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        adj = defaultdict(list)

        for i, e in enumerate(edges):
            heapq.heappush(adj[e[0]], [-succProb[i], e[1]])
            heapq.heappush(adj[e[1]], [-succProb[i], e[0]])

        curr = [[-1, start]]
        while curr:
            currProb, node = heapq.heappop(curr)
            if node == end:
                return -currProb
            while adj[node]:
                nextProb, nextNode = heapq.heappop(adj[node])
                heapq.heappush(curr, [currProb * -nextProb, nextNode])

        return 0