# There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

# There is a meeting for the representatives of each city. The meeting is in the capital city.

# There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

# A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

# Return the minimum number of liters of fuel to reach the capital city.

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)

        for r1, r2 in roads:
            adj[r1].append(r2)
            adj[r2].append(r1)

        self.res = 0
        def dfs(curr, prev):
            passengers = 0
            for n in adj[curr]:
                if n != prev:
                    p = dfs(n, curr)
                    self.res += math.ceil(p / seats)
                    passengers += p
            return passengers + 1

        dfs(0, -1)
        return self.res