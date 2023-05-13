# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

# horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
# verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7

        horizontalCuts.sort(reverse=True)
        verticalCuts.sort(reverse=True)
        maxH = maxV = 0
        prevH, prevV = h, w
        for hc in horizontalCuts:
            maxH = max(maxH, prevH - hc)
            prevH = hc
        maxH = max(maxH, prevH)
        for vc in verticalCuts:
            maxV = max(maxV, prevV - vc)
            prevV = vc
        maxV = max(maxV, prevV)
        return (maxH * maxV) % MOD
