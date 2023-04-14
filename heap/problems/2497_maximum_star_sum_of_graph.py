# There is an undirected graph consisting of n nodes numbered from 0 to n - 1. You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.

# You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

# A star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. In other words, it is a subset of edges of the given graph such that there exists a common node for all edges.

# The image below shows star graphs with 3 and 4 neighbors respectively, centered at the blue node.

# The star sum is the sum of the values of all the nodes present in the star graph.

# Given an integer k, return the maximum star sum of a star graph containing at most k edges.

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:

        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append([vals[e2], e2])
            adj[e2].append([vals[e1], e1])

        maxSum = max(vals)
        for node in adj:
            K = k
            adj[node].sort()
            currSum = vals[node]
            i = len(adj[node]) - 1
            while K > 0 and i >= 0:
                if vals[adj[node][i][1]] <= 0:
                    break
                currSum += vals[adj[node][i][1]]
                i -= 1
                K -= 1

            maxSum = max(maxSum, currSum)
        return maxSum
