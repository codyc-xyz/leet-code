# You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

# You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

# You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

# Return the maximum total importance of all roads possible after assigning the values optimally.

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        adj = defaultdict(list)

        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        lengths = []
        heapq.heapify(lengths)
        for res in adj:
            heapq.heappush(lengths, [-len(adj[res]), res])

        vals = [None] * (n)
    
        while lengths:
            _, city = heapq.heappop(lengths)
            vals[city] = n
            n -= 1
        ans = 0
        for a, b in roads:
            ans += vals[a] + vals[b]
        return ans


