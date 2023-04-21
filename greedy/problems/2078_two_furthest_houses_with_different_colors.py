# There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

# Return the maximum distance between two houses with different colors.

# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        l, r = 0, len(colors) - 1

        if colors[l] != colors[r]:
            return r - l
        L, R = l, r
        while colors[l] == colors[r]:
            r -= 1
        res1 = r - l

        while colors[L] == colors[R]:
            L += 1
        
        res2 = R - L

        return max(res1, res2)