# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:


        self.ans = 0
        seen = set()
        count = collections.Counter(tiles)
        def backtrack(i, curr):
            if i == len(tiles):
                if len(curr) > 0 and curr not in seen:
                    self.ans += 1
                    seen.add(curr)
                return
            for j in range(len(tiles)):
                if count[tiles[j]] > 0:
                    count[tiles[j]] -= 1
                    backtrack(i + 1, curr + tiles[j])
                    count[tiles[j]] += 1
                    backtrack(i + 1, curr)
        backtrack(0, "")
        return self.ans

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()
        def backtrack(curr, arr):
            if curr:
                seen.add(curr)
            if not arr:
                return
            for i in range(len(arr)):
                backtrack(curr + arr[i], arr[:i] + arr[i + 1:])
        backtrack("", tiles)
        return len(seen)