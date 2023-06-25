# We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for p1, p2 in dislikes:
            adj[p1].append(p2)
            adj[p2].append(p1)
        seen = [None for _ in range(n + 1)]

        def dfs(curr, group):
            if seen[curr] is not None:
                return seen[curr] == group
            seen[curr] = group
            return all(dfs(p, not group) for p in adj[curr])

                
        for i in range(1, n + 1):
            if seen[i] == None:
                if not dfs(i, True):
                    return False
            
        return True
