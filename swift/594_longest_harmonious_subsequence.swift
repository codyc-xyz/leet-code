/**
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
**/

class Solution {
    func findLHS(_ nums: [Int]) -> Int {
        var ans: Int = 0
        var count = [Int: Int]()

        for n in nums {
            count[n, default: 0]+=1
        }
    
        for (num, cnt) in count {
            if let nextCount = count[num+1] {
                ans = max(ans, cnt + nextCount)
            }
            if let prevCount = count[num-1] {
                ans = max(ans, cnt + prevCount)
            }
        }
        return ans
    }
}