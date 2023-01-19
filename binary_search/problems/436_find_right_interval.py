# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = [-1] * len(intervals)
        for i in range(len(intervals)):
            intervals[i].append(i)
        intervals.sort(key=lambda x: (x[0], x[1]))
                
        for i in range(1, len(intervals)):
            j = i
            while j < len(intervals):
                if intervals[i - 1][1] <= intervals[j][0]:
                    ans[intervals[i - 1][2]] = intervals[j][2]
                    break
                j += 1
        return ans

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = [-1] * len(intervals)
        for i in range(len(intervals)):
            intervals[i].append(i)
        intervals.sort(key=lambda x: (x[0], x[1]))
                
        for i in intervals:
            l, r = 0, len(intervals)
            while l < r:
                m = (l + r) // 2
                if i[1] > intervals[m][0]:
                    l = m + 1
                else:
                    r = m
            if l != len(intervals):
                ans[i[2]] = intervals[l][2]
        return ans