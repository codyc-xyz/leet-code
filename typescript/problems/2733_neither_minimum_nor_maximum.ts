// Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

// Return the selected integer.

function findNonMinOrMax(nums: number[]): number {
    const maxN: number = Math.max(...nums);
    const minN: number = Math.min(...nums);

    for (const n of nums) {
        if (n !== maxN && n !== minN) {
            return n
        }
    }
    return -1
};