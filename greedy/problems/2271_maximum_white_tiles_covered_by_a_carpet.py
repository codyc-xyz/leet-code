# You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

# You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

# Return the maximum number of white tiles that can be covered by the carpet.

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = j = 0
        if carpetLen >= tiles[-1][1]:
            return sum(1 + r - l for l, r in tiles)
        q = n = j = currSum = maxSum = 0
        for i in range(tiles[-1][1] + 1):
            if i >= tiles[j][0] and i <= tiles[j][1]:
                currSum += 1
                maxSum = max(maxSum, currSum)
            if i == tiles[j][1] and j < len(tiles):
                j += 1
            if i >= carpetLen - 1:
                if n >= tiles[q][0] and n <= tiles[q][1]:
                    currSum -= 1
                if n == tiles[q][1] and q < len(tiles):
                    q += 1
                n += 1
                    
            
        return maxSum
            
