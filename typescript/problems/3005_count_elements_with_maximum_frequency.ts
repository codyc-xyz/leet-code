/**
 You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
 */

function maxFrequencyElements(nums: number[]): number {
    
    let count: Record<number, number> = {};
    let maxCount: number = 0;
    let ans: number = 0;
    for (const n of nums) {
        if (count[n] === undefined) {
            count[n] = 0
        }
        count[n] += 1
        maxCount = Math.max(maxCount, count[n])
    }
    for (const val of Object.values(count)) {
        if (val === maxCount) {
            ans += maxCount
        }
    }
    return ans
};