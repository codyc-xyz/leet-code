# There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.

# You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.

# Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:

        heap = []
        i = applesEaten = 0
        while True:
            if i < len(days):
                for _ in range(apples[i]):
                    heapq.heappush(heap, i + days[i])
            while heap and i >= heap[0]:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                applesEaten += 1
            elif not heap and i >= len(days):
                break
            i += 1
        return applesEaten
