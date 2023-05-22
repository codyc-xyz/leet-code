# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        skipped = ans = j = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[j][1]:
                ans += 1
                if intervals[i][1] < intervals[j][1]:
                    j = i
                    skipped = 0
                else:
                    skipped += 1
                continue
            j += 1 + skipped
            skipped = 0
        return ans