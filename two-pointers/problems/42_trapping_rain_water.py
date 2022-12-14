# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        lMax = rMax = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= lMax:
                    lMax = height[l]
                else:
                    ans += lMax - height[l]
                l += 1
            else:
                if height[r] >= rMax:
                    rMax = height[r]
                else:
                    ans += rMax - height[r]
                r -= 1
        return ans