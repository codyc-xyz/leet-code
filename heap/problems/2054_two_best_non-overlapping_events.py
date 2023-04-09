# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

# Return this maximum sum.

# Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key=lambda x: x[0])
        heaps = defaultdict(list)
        for index, (start, end, value) in enumerate(events):
            for h in heaps:
                if start > heaps[h][0][0]:
                    if len(heaps[h]) > 1:
                        if value > heaps[h][-1][1]:
                            heaps[h].pop()
                        else:
                            continue
                    heapq.heappush(heaps[h], (end, value))
            heapq.heappush(heaps[index], (end, value))

        maxVal = 0
        for h in heaps:
            curr = 0
            heap = []
            for end, val in heaps[h]:
                heapq.heappush(heap, val)
                curr += val
                if len(heap) > 2:
                    curr -= heapq.heappop(heap)
            maxVal = max(maxVal, curr)
        
        return maxVal



               


          
    

