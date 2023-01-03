# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = [0] * len(temperatures)
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                idx = stack[-1][1]
                ans[idx] = i - idx
                stack.pop()
            stack.append([n,i])
        return ans

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = []
        for i in range(len(temperatures) -1, -1, -1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if stack:
                ans.append(stack[-1][0] - i)
            else:
                ans.append(0)
                
            stack.append([i, temperatures[i]])
        return ans[::-1]