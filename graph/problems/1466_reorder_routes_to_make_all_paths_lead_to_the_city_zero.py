# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adj = defaultdict(list)
        hm = defaultdict(list)

        for c1, c2 in connections:
            adj[c1].append(c2)
            adj[c2].append(c1)
            hm[c1].append(c2)

        self.ans = 0
        def dfs(curr, prev):
            if prev in hm and curr in hm[prev]:
                self.ans += 1
            for n in adj[curr]:
                if n != prev:
                    dfs(n, curr)

        dfs(0, -1)
        return self.ans