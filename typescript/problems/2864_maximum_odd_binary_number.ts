/**
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

 */

function maximumOddBinaryNumber(s: string): string {
    let count: Record<string, number> = {};
    let ans: string = "";
    for (const c of s) {
        if (c in count) {
            count[c] += 1
        }
        else {
            count[c] = 1;
        }
    }
    while (count['1'] > 1) {
        ans += '1'
        count['1'] -= 1
    }
    if ('0' in count) {
        while (count['0'] > 0) {
            ans += '0'
            count['0'] -= 1
        }

    }
    return ans + '1'

};