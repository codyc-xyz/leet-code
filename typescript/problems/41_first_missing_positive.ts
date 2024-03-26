/**
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
 */

function firstMissingPositive(nums: number[]): number {
    nums.sort((a, b) => a - b)

    let j: number = 1;
    let prev: number = -1;

    for (const n of nums) {
        if (n <= 0 || n === prev) {
            continue
        }
        if (n != j) {
            return j
        }
        j += 1
        prev = n
    }
    if (nums[nums.length - 1] === j) {
        return j + 1
    }
    return j
};