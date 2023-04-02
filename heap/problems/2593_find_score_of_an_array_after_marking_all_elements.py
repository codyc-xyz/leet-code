# You are given an array nums consisting of positive integers.

# Starting with score = 0, apply the following algorithm:

# Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
# Add the value of the chosen integer to score.
# Mark the chosen element and its two adjacent elements if they exist.
# Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.

class Solution:
    def findScore(self, nums: List[int]) -> int:

        marked = set()
        heap = defaultdict(list)
        vals = []
        for i, n in enumerate(nums):
            heapq.heappush(heap[n], i)
            heapq.heappush(vals, n)

        score = 0
        while vals:
            curr = heapq.heappop(vals)
            
            while heap[curr] and heap[curr][0] in marked:
                heapq.heappop(heap[curr])

            if heap[curr]:
                score += curr
                idx = heapq.heappop(heap[curr])
                marked.add(idx)
                marked.add(idx + 1)
                marked.add(idx - 1)

        return score


