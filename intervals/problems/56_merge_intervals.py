# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        ans = []
        for i, (l, r) in enumerate(intervals):
            if ans and l <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], r)
            else:
                ans.append([l, r])
        return ans
