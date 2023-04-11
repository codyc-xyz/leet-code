# There are two mice and n different types of cheese, each type of cheese should be eaten by exactly one mouse.

# A point of the cheese with index i (0-indexed) is:

# reward1[i] if the first mouse eats it.
# reward2[i] if the second mouse eats it.
# You are given a positive integer array reward1, a positive integer array reward2, and a non-negative integer k.

# Return the maximum points the mice can achieve if the first mouse eats exactly k types of cheese.

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        eaten = [False] * len(reward1)
        heap = []
        i = 0
        for r1, r2 in zip(reward1, reward2):
            heapq.heappush(heap, (-r1 + r2, i))
            i += 1

        ans = 0
        while k > 0:
            _, i = heapq.heappop(heap)
            ans += reward1[i]
            eaten[i] = True
            k -= 1
        
        for i in range(len(reward2)):
            if eaten[i] == True:
                continue
            else:
                ans += reward2[i]
        return ans