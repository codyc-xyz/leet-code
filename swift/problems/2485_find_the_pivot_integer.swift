/**
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
**/

class Solution {
    func pivotInteger(_ n: Int) -> Int {
        var pSum: [Int] = [0]

        for i in 1...n {
            pSum.append(pSum.last! + i)
        }

        for i in 1...pSum.count-1 {
            if pSum[i] == pSum.last! - pSum[i-1] {
                return i
            }
        }
        return -1
    }
}