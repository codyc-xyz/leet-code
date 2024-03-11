/**
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
**/

class Solution {
    func intersection(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        let N1: Set<Int> = Set(nums1)
        let N2: Set<Int> = Set(nums2)
        var ans: [Int] = []

        for n in N1 {
            if N2.contains(n) {
                ans.append(n)
            }
        }
        return ans
    }
}