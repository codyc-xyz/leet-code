# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        heapq.heapify(points)
        ans = 0
        while points:
            s, e = heapq.heappop(points)
            while points and points[0][0] <= e:
                start, end = heapq.heappop(points)
                if end < e:
                    e = end
            ans += 1
        return ans

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()
        end = points[0][1]
        ans = 1
        for i in range(len(points)):
            s, e = points[i]
            if s <= end:
                if e < end:
                    end = e
                continue
            end = e
            ans += 1
        return ans
