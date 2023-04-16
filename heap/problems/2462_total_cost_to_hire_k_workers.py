# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

# You will run k sessions and hire exactly one worker in each session.
# In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
# For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
# In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
# If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
# A worker can only be chosen once.
# Return the total cost to hire exactly k workers.

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        ans = 0
        heap = []
        i, j = 0, n - 1
        while i < candidates:
            heapq.heappush(heap, [costs[i], i, 1])
            i += 1

        while j >= max(i, n - candidates):
            heapq.heappush(heap, [costs[j], j, -1])
            j -= 1
        

        while k > 0:
            val, idx, direction = heapq.heappop(heap)
            ans += val
            if i <= j:
                if direction == -1:
                    heapq.heappush(heap, [costs[j], j, -1])
                    j -= 1
                elif direction == 1:
                    heapq.heappush(heap, [costs[i], i, 1])
                    i += 1
            k -= 1
        return ans
           
