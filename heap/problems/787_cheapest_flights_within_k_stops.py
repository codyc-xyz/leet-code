# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for frm, to, price in flights:
            heapq.heappush(adj[frm], [price, to])

        heap = [[0, 0, src]]
        seen = set()
        while heap:
            price, dist, loc = heapq.heappop(heap)
            if loc == dst:
                return price
            if (dist, loc) in seen or dist > k:
                continue
            seen.add((dist, loc))
            for p, to in adj[loc]:
                heapq.heappush(heap, [price + p, dist + 1, to])
        return -1