# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        ans = []
        def backtrack(i, path):
            if i == len(graph) - 1:
                ans.append(path)
                return
            for j in graph[i]:
                path.append(j)
                backtrack(j, path[:])
                path.pop()
        backtrack(0, [0])
        return ans