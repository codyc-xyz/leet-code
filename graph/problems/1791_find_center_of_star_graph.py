# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = collections.Counter()
        for e1, e2 in edges:
            count[e1] += 1
            count[e2] += 1

        maxCount, ans = 0, None
        for c in count:
            if count[c] > maxCount:
                maxCount = count[c]
                ans = c
        return ans