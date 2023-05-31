# There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

# The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0
        adj = defaultdict(list)
        cities = []
        for r1, r2 in roads:
            adj[r1].append(r2)
            adj[r2].append(r1)
            if r1 not in cities:
                cities.append(r1)
            if r2 not in cities:
                cities.append(r2)

        
        def networkRank(city1, city2):
            res = 0
            for c1 in adj[city1]:
                if (city1, c1) not in seen and (c1, city1) not in seen:
                    res += 1
                    seen.add((city1, c1))

            for c2 in adj[city2]:
                if (city2, c2) not in seen and (c2, city2) not in seen:
                    res += 1
                    seen.add((city2, c2))
                
            return res
            
        ans = 0
        for i in range(len(cities)):
            for j in range(i, len(cities)):
                seen = set()
                ans = max(ans, networkRank(cities[i], cities[j]))
        return ans



