/**
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
**/

class Solution {
    func findMinArrowShots(_ points: [[Int]]) -> Int {
        var points: [[Int]] = points
        var ans: Int = 1
        points.sort(by: { (a: [Int], b: [Int]) -> Bool in
            return a[1] < b[1]
        })
        var currEnd: Int = points[0][1]

        for i in 0...points.count-1 {
            if points[i][0] > currEnd {
                currEnd = points[i][1]
                ans += 1
            }
        }
        return ans
    }
}