# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        seen = [0 for _ in range(len(graph))]
        def dfs(curr):
            if seen[curr] != 0:
                return seen[curr] == 1
            seen[curr] = -1
            for n in graph[curr]:
                if not dfs(n):
                    return False
            seen[curr] = 1
            return True
               
        ans = []
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)

        return ans
