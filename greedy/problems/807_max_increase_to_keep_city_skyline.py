# There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.

# A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.

# We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.

# Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        Xs = defaultdict(list)
        Ys = defaultdict(list)
        ans = 0
        for x in range(row):
            for y in range(col):
                heapq.heappush(Xs[x], -grid[x][y])
                heapq.heappush(Ys[y], -grid[x][y])

        for x in range(row):
            for y in range(col):
                ans += -max(Xs[x][0], Ys[y][0]) - grid[x][y]

        return ans