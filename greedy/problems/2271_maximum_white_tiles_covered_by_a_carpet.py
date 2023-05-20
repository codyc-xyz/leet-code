# You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

# You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

# Return the maximum number of white tiles that can be covered by the carpet.

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()

        j = curr = ans = 0
        for i in range(len(tiles)):
            while j < len(tiles) and tiles[j][1] - tiles[i][0] < carpetLen:
                curr += tiles[j][1] - tiles[j][0] + 1
                j += 1
            if j < len(tiles) and tiles[j][0] - tiles[i][0] < carpetLen:
                ans = max(ans, curr + carpetLen - (tiles[j][0] - tiles[i][0]))
            else:
                ans = max(ans, curr)
            if j != i:
                curr -= tiles[i][1] - tiles[i][0] + 1
            j = max(j, i + 1)
        return ans            
