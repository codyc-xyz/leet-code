# You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.

# All gardens have at most 3 paths coming into or leaving it.

# Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

# Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        adj = defaultdict(list)

        for n1, n2 in paths:
            adj[n1].append(n2)
            adj[n2].append(n1)

        hm = {}
        def dfs(curr, val):
            length = len(adj[curr])
            for nei in adj[curr]:
                if nei in hm and hm[nei] == val:
                    break
                length -= 1
            return length == 0

        for i in range(1, n + 1):
            for j in range(1, 5):
                if dfs(i, j):
                    hm[i] = j
                    break

        ans = [None for _ in range(n)]

        for n in hm:
            ans[n - 1] = hm[n]
        return ans