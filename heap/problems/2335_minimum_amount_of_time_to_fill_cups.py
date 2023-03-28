# You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

# You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount = [a * -1 for a in amount]
        heapq.heapify(amount)
        seconds = 0
        
        while len(amount) > 1 and amount[0] < 0 and amount[1] < 0:
            curr1 = heapq.heappop(amount)
            curr2 = heapq.heappop(amount)
            if curr1 < -1:
                heapq.heappush(amount, curr1 + 1)
            if curr2 < -1:
                heapq.heappush(amount, curr2 + 1)
            seconds += 1
            
        return seconds + abs(amount[0]) if amount else seconds
        

        