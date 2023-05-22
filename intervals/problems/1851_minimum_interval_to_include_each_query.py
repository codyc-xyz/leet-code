# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

# You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

# Return an array containing the answers to the queries.

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        for i, (l, r) in enumerate(intervals):
            intervals[i].append(r - l + 1)

        for i, q in enumerate(queries):
            queries[i] = [q, i]
        intervals.sort()
        queries.sort()
        ans = [None for _ in range(len(queries))]
        j = 0
        heap = []
        for q, i in queries:
            while j < len(intervals) and q > intervals[j][1]:
                j += 1
            while j < len(intervals) and intervals[j][0] <= q:
                heapq.heappush(heap, [intervals[j][2], intervals[j][1]])
                j += 1
            while heap and q > heap[0][1]:
                heapq.heappop(heap)
            ans[i] = heap[0][0] if heap else -1

        return ans
