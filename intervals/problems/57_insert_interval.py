# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        if not intervals:
            return [newInterval]
        if right < intervals[0][0]:
            return [newInterval] + intervals
        elif left > intervals[-1][1]:
            return intervals + [newInterval]
        skips = 0
        ans = []
        for i, (l, r) in enumerate(intervals):
            if i > 0 and left > intervals[i - 1][1] and right < l:
                ans.append(newInterval)
            if skips > 0:
                skips -=1
                continue
            if left <= l and right >= l:
                intervals[i] = [left, max(right, r)]
                j = i + 1
                while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
                    intervals[i][1] = max(intervals[i][1], intervals[j][1])
                    skips += 1
                    j += 1

            elif left >= l and left <= r:
                intervals[i] = [l, max(right, r)]
                j = i + 1
                while j < len(intervals) and intervals[i][1] >= intervals[j][0]:

                    intervals[i][1] = max(intervals[i][1], intervals[j][1])
                    skips += 1
                    j += 1
            ans.append(intervals[i])

        
        return ans
