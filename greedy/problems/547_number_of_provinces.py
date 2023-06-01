# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS = len(isConnected)
        COLS = len(isConnected[0])
        adj = defaultdict(list)

        for i in range(ROWS):
            for j in range(COLS):
                if isConnected[i][j] and j + 1 not in adj[i + 1]:
                    adj[i + 1].append(j + 1)
                    adj[j + 1].append(i + 1)
                    

        def dfs(curr):
            if curr in seen:
                return 0
            seen.add(curr)
            for n in adj[curr]:
                if n not in seen:
                    dfs(n)
            return 1


        seen = set()
        ans = 0
        for i in range(1, ROWS + 1): 
            ans += dfs(i) 
            if len(seen) == ROWS:
                break
        return ans              