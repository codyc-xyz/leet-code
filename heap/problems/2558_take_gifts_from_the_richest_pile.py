# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

# Choose the pile with the maximum number of gifts.
# If there is more than one pile with the maximum number of gifts, choose any.
# Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
# Return the number of gifts remaining after k seconds.

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        maxHeap = [-1 * g for g in gifts]
        heapq.heapify(maxHeap)
        while k > 0:
            heapq.heappush(maxHeap, (int(math.sqrt(heapq.heappop(maxHeap) * -1))) * -1)
            k -= 1
        return sum(maxHeap) * -1
