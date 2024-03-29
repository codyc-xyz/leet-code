# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        blueAdj = defaultdict(list)
        redAdj = defaultdict(list)

        for n1, n2 in redEdges:
            redAdj[n1].append(n2)

        for n1, n2 in blueEdges:
            blueAdj[n1].append(n2)

        ans = [float('inf') for _ in range(n)] 

        qR = deque([(0, True, 0)])
        qB = deque([(0, False, 0)])
        minDepth = float('inf')
        while qR or qB:
            if qR:
                currR, colR, depthR = qR.popleft()
            if qB:
                currB, colB, depthB = qB.popleft()
            ans[currR] = min(ans[currR], depthR)
            ans[currB] = min(ans[currB], depthB)
            while blueAdj[currR]:
                qB.append((blueAdj[currR].pop(), not colR, depthR + 1))
            while redAdj[currB]:
                qR.append((redAdj[currB].pop(), not colB, depthB + 1))

        for i, n in enumerate(ans):
            if n == float('inf'):
                ans[i] = -1
        return ans