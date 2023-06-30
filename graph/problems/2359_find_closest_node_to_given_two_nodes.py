# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

# You are also given two integers node1 and node2.

# Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

# Note that edges may contain cycles.

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        adj = defaultdict(list)
        for i, n in enumerate(edges):
            if n != -1:
                adj[i].append(n)

        minDepth = float('inf')
        ans = -1
        q1 = deque([(node1, 0)])
        seen1 = set()
        seen1.add(node1)
        depth1 = [float('inf') for _ in range(len(edges))]
        depth1[node1] = 0
        while q1:
            curr, depth = q1.popleft()
            for n in adj[curr]:
                if n not in seen1:
                    seen1.add(n)
                    depth1[n] = depth + 1
                    q1.append((n, depth + 1))

        q2 = deque([(node2, 0)])
        seen2 = set()
        seen2.add(node2)
        depth2 = [float('inf') for _ in range(len(edges))]
        depth2[node2] = 0
        while q2:
            curr, depth = q2.popleft()
            for n in adj[curr]:
                if n not in seen2:
                    seen2.add(n)
                    depth2[n] = depth + 1
                    q2.append((n, depth + 1))
        i = 0
        for a, b in zip(depth1, depth2):
            if max(a, b) < minDepth:
                ans = i
                minDepth = max(a, b)
            i += 1
        return ans


