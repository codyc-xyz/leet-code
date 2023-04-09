# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

# Return this maximum sum.

# Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        heap = []
        bestSum = maxVal = 0
        for s, e, v in events:
            while heap and s > heap[0][0]:
                maxVal = max(maxVal, heapq.heappop(heap)[1])

            bestSum = max(bestSum, maxVal + v)
            heapq.heappush(heap, [e, v])

        return bestSum


               


          
    

