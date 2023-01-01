# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for i, n in enumerate(heights):
            start = i
            while stack and n < stack[-1][1]:
                start, height = stack.pop()
                length = i - start
                
                ans = max(ans, height * length)
            stack.append([start, n])
        
        while stack:
            start, height = stack.pop()
            length = len(heights) - start
            ans = max(ans, height * length)

        
        return ans