# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costHeap = [[-abs(costs[i][0] - costs[i][1]), costs[i][0], costs[i][1]] for i in range(len(costs))]
        heapq.heapify(costHeap)

        target = len(costs) // 2
        a = 0
        b = 0
        ans = 0
        while costHeap:
            _, costA, costB = heapq.heappop(costHeap)
            if costA < costB and a < target:
                ans += costA
                a += 1
            elif costA > costB and b < target:
                ans += costB
                b += 1
            else:
                if a > b:
                    ans += costB
                    b += 1
                else:
                    ans += costA
                    a += 1
        return ans

