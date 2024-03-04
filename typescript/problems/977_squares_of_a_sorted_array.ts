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

function sortedSquares(nums: number[]): number[] {
    let ans: number[] = [];
    let l: number = 0;
    let r: number = nums.length - 1;

    while (l <= r) {
        if (Math.abs(nums[l]) > Math.abs(nums[r])) {
            ans.unshift(nums[l]**2)
            l++
        }
        else {
            ans.unshift(nums[r]**2)
            r--
        }
    }
    return ans

}