# Given the following details of a matrix with n columns and 2 rows :

# The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
# Your task is to reconstruct the matrix with upper, lower and colsum.

# Return it as a 2-D integer array.

# If there are more than one valid solution, any of them will be accepted.

# If no valid solution exists, return an empty 2-D array.

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        ans = [[0 for _ in range(len(colsum))] for _ in range(2)]

        colVals = []
        for i, c in enumerate(colsum):
            colVals.append([-c, i])

        heapq.heapify(colVals)

        while upper > 0 or lower > 0:
            num, idx = heapq.heappop(colVals)
            if num == -2:
                ans[0][idx] = 1
                ans[1][idx] = 1
                upper -= 1
                lower -= 1
            elif num == -1:
                if upper > lower:
                    ans[0][idx] = 1
                    upper -= 1
                else:
                    ans[1][idx] = 1
                    lower -= 1
            else:
                return []
        return ans
