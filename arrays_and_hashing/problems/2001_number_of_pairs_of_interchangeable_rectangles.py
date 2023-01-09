# You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

# Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

# Return the number of pairs of interchangeable rectangles in rectangles.

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = defaultdict(int)
        ans = 0
        for r in rectangles:
            w,h = r[0], r[1]
            val = w / h
            if count[val]:
                ans += count[val]
            count[val] += 1
        return ans