/**
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).
 */


function minimumLength(s: string): number {
    let l: number = 0;
    let r: number = s.length - 1;
    let ans: number = s.length;

    while (l < r) {
        if (s[l] === s[r]) {
            while (s[l] === s[r]) {
                l += 1
                ans -= 1
            }
            while (l - 1 < r && s[r] === s[l-1]) {
                r -= 1
                ans -= 1
            }
        }
        else {
            break
        }
    }
    return ans
};