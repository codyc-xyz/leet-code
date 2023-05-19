# You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

# You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

# Return the maximum number of white tiles that can be covered by the carpet.

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        pSum = [0 for _ in range(tiles[-1][1] + 1)]
        for l, r in tiles:
            for i in range(l, r + 1):
                pSum[i] = 1
        currSum = 0
        carpetLen = min(carpetLen, len(pSum))
        for i in range(carpetLen):
            currSum += pSum[i]
        maxSum = currSum
        j = 0
        for i in range(carpetLen, len(pSum)):
            currSum -= pSum[j]
            currSum += pSum[i]
            maxSum = max(maxSum, currSum)
            j += 1
        
        return maxSum
            
