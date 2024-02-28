// The minimum absolute difference of an array a is defined as the minimum value of |a[i] - a[j]|, where 0 <= i < j < a.length and a[i] != a[j]. If all elements of a are the same, the minimum absolute difference is -1.

// For example, the minimum absolute difference of the array [5,2,3,7,2] is |2 - 3| = 1. Note that it is not 0 because a[i] and a[j] must be different.
// You are given an integer array nums and the array queries where queries[i] = [li, ri]. For each query i, compute the minimum absolute difference of the subarray nums[li...ri] containing the elements of nums between the 0-based indices li and ri (inclusive).

// Return an array ans where ans[i] is the answer to the ith query.

// A subarray is a contiguous sequence of elements in an array.

// The value of |x| is defined as:

// x if x >= 0.
// -x if x < 0.

function minDifference(nums: number[], queries: number[][]): number[] {
    const N: number = nums.length;
    let res: number[][] = new Array(N+1);

    for (let i = 0; i < N + 1; i++) {
        res[i] = new Array(101).fill(0);
    }

    let ans: number[] = [];
    for (let i = 1; i < N+1; i++) {
        let n: number = nums[i-1];
        for (let j = 0; j < 101; j++) {
            if (n === j) {
                res[i][j] = res[i-1][j] + 1;
            }
            else {
                res[i][j] = res[i-1][j];
            }
        }
    }
    for (const q of queries) {
        let a: number = q[0];
        let b: number = q[1];
        let prev: number = -1;
        let currMin: number = Infinity;
        for (let i = 1; i < 101; i++) {
            if (res[b+1][i] - res[a][i] > 0) {
                if (prev != -1) {
                    currMin = Math.min(currMin, i - prev);
                }
                prev = i
            }
        }
        if (currMin !== Infinity) {
            ans.push(currMin)
        }
        else {
            ans.push(-1)
        }
    }
    return ans;
};