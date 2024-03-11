/**
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
 */

function intersection(nums1: number[], nums2: number[]): number[] {
    const N1: Set<number> = new Set(nums1);
    const N2: Set<number> = new Set(nums2);
    let ans: number[] = [];
    for (const n of N1) {
        if (N2.has(n)) {
            ans.push(n)
        }
    }
    return ans
};