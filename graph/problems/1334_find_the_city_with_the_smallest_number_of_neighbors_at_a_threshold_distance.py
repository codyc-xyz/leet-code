# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

class Solution:
    def findTheCity(self, N: int, edges: List[List[int]], distanceThreshold: int) -> int:

        adj = defaultdict(list)

        for n1, n2, weight in edges:
            adj[n1].append((weight, n2))
            adj[n2].append((weight, n1))

        numReachable = [0 for _ in range(N)]
        for i in range(N):
            heap = [(0, i)]
            seen = set()
            seen.add(i)
            while heap:
                currWeight, curr = heapq.heappop(heap)
                if curr not in seen:
                    numReachable[i] += 1
                    seen.add(curr)
                for w, n in adj[curr]:
                    if currWeight + w <= distanceThreshold and n not in seen:
                        heapq.heappush(heap, (currWeight + w, n))
                        
        minNum = float('inf')
        ans = -1
        for i in range(N - 1, -1, -1):
            if numReachable[i] < minNum:
                minNum = numReachable[i]
                ans = i

        return ans   