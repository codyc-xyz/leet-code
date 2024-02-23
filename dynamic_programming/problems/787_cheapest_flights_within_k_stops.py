# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for f, t, p in flights:
            adj[f].append((p, t))

        @cache
        def dfs(curr, depth):
            if curr == dst:
                return 0
            elif depth < 0:
                return float('inf')

            res = float('inf')
            for p, t in adj[curr]:
                res = min(res, p + dfs(t, depth - 1))
            return res
        ans = dfs(src, k)
        return ans if ans != float('inf') else -1

