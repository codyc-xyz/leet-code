# There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.

# You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.

# Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:

        heap = []
        i = applesEaten = 0
        while i < len(days) or heap:
            if i < len(days):
               heapq.heappush(heap, [i + days[i], apples[i]])
            if heap:
                while heap and heap[0][0] <= i:
                    heapq.heappop(heap)
                if heap:
                    expiry, count = heapq.heappop(heap)
                    applesEaten += 1
                    if expiry > i + 1 and count > 1:
                        heapq.heappush(heap, [expiry, count - 1])
            i += 1
        return applesEaten 
