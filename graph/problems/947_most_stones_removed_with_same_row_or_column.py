# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        rows = defaultdict(list)
        cols = defaultdict(list)

        for r, c in stones:
            rows[r].append(c)
            cols[c].append(r)
            
        def dfs(r, c):
            if (r, c) in seen:
                return 
            seen.add((r, c))
            for col in rows[r]:
                if (r, col) in seen:
                    continue
                dfs(r, col)
            for row in cols[c]:
                if (row, c) in seen:
                    continue
                dfs(row, c)

        seen = set()
        components = 0
        for r, c in stones:
            if (r, c) not in seen:
                dfs(r, c)
                components += 1

        return len(seen) - components
