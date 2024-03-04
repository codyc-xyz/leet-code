/**
 Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 */

function sortedSquares(nums: number[]): number[] {
    let ans: number[] = [];

    for (const n of nums) {
        ans.push(n**2)
    }
    ans.sort((a, b) => a - b);
    return ans
};