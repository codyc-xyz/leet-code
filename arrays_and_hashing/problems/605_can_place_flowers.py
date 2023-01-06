# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if len(flowerbed) < 3:
            if 1 not in flowerbed:
                n -= 1
                return n <= 0
            return not n
        
        elif len(flowerbed) == 3:
            for i in range(len(flowerbed) - 2):
                if i == 0 and not flowerbed[i] and not flowerbed[i + 1] and not flowerbed[i + 2]:
                    n -= 2
                    return n <= 0
                elif not flowerbed[i] and not flowerbed[i + 1]:
                    n -= 1
                    return not n
                
        for i in range(len(flowerbed)):
            if i == 0:
                if not flowerbed[i] and not flowerbed[i + 1]:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed) - 1:
                if not flowerbed[i - 1] and not flowerbed[i]:
                    flowerbed[i] = 1
                    n -= 1
            elif not flowerbed[i - 1] and not flowerbed[i] and not flowerbed[i + 1]:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False