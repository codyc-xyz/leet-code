/**
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
 */

function pivotInteger(n: number): number {
    let pSum: number[] = [0];

    for (let i = 1; i <= n; i++) {
        pSum.push(pSum[pSum.length-1] + i)
    }

    for (let i = 1; i < pSum.length; i++) {
        if (pSum[i] === pSum[pSum.length-1] - pSum[i-1]) {
            return i
        }
    }
    return -1
};