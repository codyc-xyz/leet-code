# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        count = collections.Counter(hand)
        heap = []
        for c in count:
            heapq.heappush(heap, [c, count[c]])

        addBack = []
        seen = set()

        while heap:
            N, countN = heapq.heappop(heap)
            if not seen or N - 1 in seen:
                seen.add(N)
                if countN > 1:
                    addBack.append([N, countN - 1])
            else:
                addBack.append([N, countN])
            if len(seen) == groupSize:
                seen = set()
                for num, countNum in addBack:
                    heapq.heappush(heap, [num, countNum])
                addBack = []
        return False if seen or addBack else True

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = collections.Counter(hand)
        heap = []
        for c in count:
            heapq.heappush(heap, c)

        while heap:
            minN = heap[0]

            for i in range(minN, groupSize + minN):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
                    del count[i]
        return True
                
                