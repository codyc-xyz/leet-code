# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

# Return the maximum number of events you can attend.

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        for i, e in enumerate(events):
            e.append(i)
        endFirstEvents = [[e, s, i] for s, e, i in events]
        
        heapq.heapify(events)
        heapq.heapify(endFirstEvents)
        seen = set()
        i = 1
        ans = 0
        while endFirstEvents:
            while (endFirstEvents and i > endFirstEvents[0][0]) or (endFirstEvents and endFirstEvents[0][2] in seen):
                heapq.heappop(endFirstEvents)
            if endFirstEvents and i >= endFirstEvents[0][1]:
                _, _, j = heapq.heappop(endFirstEvents)
                seen.add(j)
                ans += 1
            else:
                while (events and events[0][2] in seen) or (events and i > events[0][1]):
                    heapq.heappop(events)
                if events and events[0][0] <= i:
                    _, _, j = heapq.heappop(events)
                    seen.add(j)
                    ans += 1
            i += 1
        return ans


