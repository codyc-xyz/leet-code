# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj = defaultdict(list)
        vals = set()
        for i, (e1, e2) in enumerate(equations):
            adj[e1].append((e2, values[i]))
            adj[e2].append((e1, 1 / values[i]))
            vals.add(e1)
            vals.add(e2)

        def dfs(curr, target, path):
            if self.res:
                return
            if curr == target and curr in vals and target in vals:
                self.res = 1
                for n in path:
                    self.res *= n
                return
            seen.add(curr)
            for c, val in adj[curr]:
                if c not in seen:
                    dfs(c, target, path + [val])

        ans = []
        for curr, target in queries:
            self.res = None
            seen = set()
            dfs(curr, target, [])
            if self.res != None:
                ans.append(self.res)
            else:
                ans.append(-1)

        return ans
