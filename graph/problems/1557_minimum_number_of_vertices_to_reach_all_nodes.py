# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

# Notice that you can return the vertices in any order.

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        incoming = [False for _ in range(n)]

        for e1, e2 in edges:
            incoming[e2] = True

        ans = []
        for i in range(n):
            if not incoming[i]:
                ans.append(i)
        return ans


