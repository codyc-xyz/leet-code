# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if len(bloomDay) < m * k:
            return -1
        
        def makeBouquets(mid):
            i = countK = countM = 0
            while i < len(bloomDay):
                if bloomDay[i] <= mid:
                    countK += 1
                else:
                    countK = 0
                if countK == k:
                    countM += 1
                    countK = 0
                i += 1
            return countM >= m
                
        l, r = 0, max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            if makeBouquets(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return l