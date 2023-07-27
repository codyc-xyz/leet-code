# You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

# Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

# Note that the batteries cannot be recharged.

# Return the maximum number of minutes you can run all the n computers simultaneously.

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        batteryHeap = [-b for b in batteries]
        heapq.heapify(batteryHeap)
        inUse = []
        for i in range(n):
            if batteryHeap[0] < 0:
                inUse.append(heapq.heappop(batteryHeap) + 1)
            else:
                return 0
        ans = 1
        while len(batteryHeap) + len(inUse) >= n:
            while inUse:
                curr = inUse.pop()
                if curr < 0:
                    heapq.heappush(batteryHeap, curr)

            while batteryHeap and len(inUse) < n:
                inUse.append(heapq.heappop(batteryHeap) + 1)

            if len(inUse) == n:
                ans += 1
            else:
                return ans
        return ans
