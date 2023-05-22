# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

# You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

# Return an array containing the answers to the queries.

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        for i, (l, r) in enumerate(intervals):
            intervals[i].append(r - l + 1)

        intervals.sort(key=lambda x: [x[2]])
        ans = []
        for q in queries:
            j = 0
            while j < len(intervals) and (q > intervals[j][1] or q < intervals[j][0]):
                j += 1
            if j < len(intervals):
                ans.append(intervals[j][2])
            else:
                ans.append(-1)
        return ans
