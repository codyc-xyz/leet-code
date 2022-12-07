# Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

# Every house can be warmed, as long as the house is within the heater's warm radius range. 

# Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

# Notice that all the heaters follow your radius standard, and the warm radius will the same.

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = a = 0
        while a < len(houses):
            b = 0
            maxDist = float("inf")
            while b < len(heaters):
                dist = abs(heaters[b] - houses[a])
                maxDist = (min(maxDist, dist))
                b += 1
            res = max(res, maxDist)
            a += 1
        return res