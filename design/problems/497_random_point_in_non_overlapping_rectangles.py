# You are given an array of non-overlapping axis-aligned rectangles rects where rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner point of the ith rectangle and (xi, yi) is the top-right corner point of the ith rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.

# Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.

# Note that an integer point is a point that has integer coordinates.

# Implement the Solution class:

# Solution(int[][] rects) Initializes the object with the given rectangles rects.
# int[] pick() Returns a random integer point [u, v] inside the space covered by one of the given rectangles.

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.points = []
        for a, b, x, y in rects:
            for i in range(a, x+1):
                for j in range(b,y+1):
                    self.points.append([i,j])

    def pick(self) -> List[int]:
        return self.points[random.randint(0, len(self.points) - 1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()