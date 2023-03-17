# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

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