/**
 We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
*/

function findLHS(nums: number[]): number {
    let ans: number = 0
    let count: Record<number, number> = {}

    for (const n of nums) {
        if (count[n] === undefined) {
            count[n] = 0
        }
        count[n]++
    }
    const keys: string[] = Object.keys(count)
    for (const key of keys) {
        const curr = count[key]
        const minusOne = String(Number(key) - 1)
        const plusOne = String(Number(key) + 1)
        if (count[minusOne] !== undefined) {
            ans = Math.max(ans, curr + count[minusOne])
        }
        if (count[plusOne] !== undefined) {
            ans = Math.max(ans, curr + count[plusOne])
        }
    }
    return ans
};