# You are given a 0-indexed 2D integer array grid of size m x n that represents a map of the items in a shop. The integers in the grid represent the following:

# 0 represents a wall that you cannot pass through.
# 1 represents an empty cell that you can freely move to and from.
# All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.
# It takes 1 step to travel between adjacent grid cells.

# You are also given integer arrays pricing and start where pricing = [low, high] and start = [row, col] indicates that you start at the position (row, col) and are interested only in items with a price in the range of [low, high] (inclusive). You are further given an integer k.

# You are interested in the positions of the k highest-ranked items whose prices are within the given price range. The rank is determined by the first of these criteria that is different:

# Distance, defined as the length of the shortest path from the start (shorter distance has a higher rank).
# Price (lower price has a higher rank, but it must be in the price range).
# The row number (smaller row number has a higher rank).
# The column number (smaller column number has a higher rank).
# Return the k highest-ranked items within the price range sorted by their rank (highest to lowest). If there are fewer than k reachable items within the price range, return all of them.

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        dq = deque([(start[0], start[1], 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        seen.add((start[0], start[1]))
        heap = []
        while dq:
    
            x, y, dist = dq.popleft()
            if grid[x][y] == 0:
                continue
            elif grid[x][y] != 1 and pricing[0] <= grid[x][y] <= pricing[1]:
                heapq.heappush(heap, [dist, grid[x][y], x, y])
            for dx, dy in directions:
                if 0 <= x + dx < row and 0 <= y + dy < col and (x + dx, y + dy) not in seen:
                    dq.append([x + dx, y + dy, dist + 1])
                    seen.add((x + dx, y + dy))

        ans = []
        while heap and k > 0:
            _, _, x, y = heapq.heappop(heap)
            ans.append([x,y])
            k -= 1
        return ans




