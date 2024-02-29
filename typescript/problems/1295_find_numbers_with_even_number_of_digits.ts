/**
  Given an array nums of integers, return how many of them contain an even number of digits.
 */

function findNumbers(nums: number[]): number {
    let ans: number = 0;
    for (const n of nums) {
        if (String(n).length % 2 === 0) {
            ans++
        }
    }
    return ans
};