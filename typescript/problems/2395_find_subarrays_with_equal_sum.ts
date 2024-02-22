// Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.

// Return true if these subarrays exist, and false otherwise.

// A subarray is a contiguous non-empty sequence of elements within an array.

function findSubarrays(nums: number[]): boolean {
    
    let count: Record<number, number> = {};

    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] + nums[i+1] in count) {
            return true
        }
        else {
            count[nums[i] + nums[i+1]] = 1
        }
    }
    return false
};