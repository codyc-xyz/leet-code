# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). 
# You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        adj = defaultdict(list)

        for i in range(rows):
            for j in range(cols):
                if i - 1 >= 0:
                    heapq.heappush(adj[(i, j)], [abs(heights[i][j] - heights[i - 1][j]), (i - 1, j)])
                if i + 1 < rows:
                    heapq.heappush(adj[(i, j)], [abs(heights[i][j] - heights[i + 1][j]), (i + 1, j)])
                if j - 1 >= 0:
                    heapq.heappush(adj[(i, j)], [abs(heights[i][j] - heights[i][j - 1]), (i, j - 1)])
                if j + 1 < cols:
                    heapq.heappush(adj[(i, j)], [abs(heights[i][j] - heights[i][j + 1]), (i, j + 1)])

        heap = [[0, (0, 0)]]
        goal = (rows - 1, cols - 1)
        while heap:
            maxDiff, pos = heapq.heappop(heap)
            if pos == goal:
                return maxDiff
            while adj[pos]:
                maxDiff1, pos1 = heapq.heappop(adj[pos])
                heapq.heappush(heap, [max(maxDiff, maxDiff1), pos1])