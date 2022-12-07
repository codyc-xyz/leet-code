# Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

# Every house can be warmed, as long as the house is within the heater's warm radius range. 

# Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

# Notice that all the heaters follow your radius standard, and the warm radius will the same.

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        a = len(houses) - 1
        b = len(heaters) - 1
        heaters.sort()
        houses.sort()
        while a >= 0:
            dist = abs(houses[a] - heaters[b])
            while b > 0 and abs(houses[a] - heaters[b - 1]) <= dist:
                b -= 1
                dist = abs(heaters[b] - houses[a])
            res = max(res, dist)
            a -= 1
        return res