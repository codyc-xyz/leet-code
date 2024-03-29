# You are given a directed graph with n nodes labeled from 0 to n - 1, where each node has exactly one outgoing edge.

# The graph is represented by a given 0-indexed integer array edges of length n, where edges[i] indicates that there is a directed edge from node i to node edges[i].

# The edge score of a node i is defined as the sum of the labels of all the nodes that have an edge pointing to i.

# Return the node with the highest edge score. If multiple nodes have the same edge score, return the node with the smallest index.

class Solution:
    def edgeScore(self, edges: List[int]) -> int:

        scores = [0 for _ in range(len(edges))]

        for i, e in enumerate(edges):
            scores[e] += i

        maxScore = -1
        ans = -1
        for i, s in enumerate(scores):
            if s > maxScore:
                maxScore = s
                ans = i
        return ans