# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        countTop = collections.Counter(tops)
        countBottom = collections.Counter(bottoms)
        maxTopCount = max(countTop.values())
        maxBottomCount = max(countBottom.values())
        res = 0
        if maxTopCount > maxBottomCount:
            maxCountKey= max(countTop, key=lambda k: countTop[k])
            for t, b in zip(tops, bottoms):
                if b == maxCountKey and t != maxCountKey:
                    res += 1
            return res if res + maxTopCount == len(tops) else -1
        else:
            maxCountKey = max(countBottom, key=lambda k: countBottom[k])
            for t, b in zip(tops, bottoms):
                if t == maxCountKey and b != maxCountKey:
                    res += 1
            return res if res + maxBottomCount == len(tops) else -1
