# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:        
        ans = 0
        stack = []  
        for i, n in enumerate(height):
            while stack and n > stack[-1][1]:
                start, height = stack.pop()
                if not stack:
                    break
                volume = min(stack[-1][1], n) - height
                ans += (i - stack[-1][0] - 1) * volume
            stack.append([i, n])
        return ans