// Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

// Return the largest lucky integer in the array. If there is no lucky integer return -1.

function findLucky(arr: number[]): number {

    arr.sort((a,b) => b - a);

    const count: Record<number, number> = {};

    for (const n of arr) {
        if (n in count) {
            count[n]++
        }
        else {
            count[n] = 1
        }
    }
    for (const n of arr) {
        if (n === count[n]) {
            return n
        }
    }
    return -1
    
};