# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

# To gain points, you must pick one cell in each row. Picking the cell at coordinates(r, c) will add points[r][c] to your score.

# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates(r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

# Return the maximum number of points you can achieve.

# abs(x) is defined as:

# x for x >= 0.
# -x for x < 0.

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        arr = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]

        for i in range(len(points[0])):
            arr[0][i] = points[0][i]

        for i in range(1, len(points)):
            for j in range(len(points[0])):
                arr[i][j] = max(points[i][j] + arr[i - 1][n] - abs(n - j)
                                for n in range(len(points[0])))

        return max(arr[-1])


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        dp = points[0]
        left, right = [0] * cols, [0] * cols
        for i in range(1, rows):
            for j in range(cols):
                if j == 0:
                    left[j] = dp[j]
                else:
                    left[j] = max(left[j - 1] - 1, dp[j])

            for n in range(cols - 1, -1, -1):
                if n == cols - 1:
                    right[n] = dp[n]
                else:
                    right[n] = max(right[n + 1] - 1, dp[n])

            for c in range(cols):
                dp[c] = points[i][c] + max(left[c], right[c])

        return max(dp)
