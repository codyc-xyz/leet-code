# You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. 
# The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

# Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:

        heap = [-a, -b, -c]
        heapq.heapify(heap)
        score = 0
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if first < 0 and second < 0:
                heapq.heappush(heap, first + 1)
                heapq.heappush(heap, second + 1)
                score += 1
                    
        return score