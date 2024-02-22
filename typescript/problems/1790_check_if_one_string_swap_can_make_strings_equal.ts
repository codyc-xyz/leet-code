// You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

// Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

function areAlmostEqual(s1: string, s2: string): boolean {

    let diffIdx: number[] = []

    for (let i = 0; i < s1.length; i++) {
        if (s1[i] != s2[i]) {
            diffIdx.push(i)
        }
    }
    if (diffIdx.length === 0) {
        return true
    }
    else if (diffIdx.length === 2 && s1[diffIdx[0]] === s2[diffIdx[1]] && s1[diffIdx[1]] === s2[diffIdx[0]]) {
        return true
    }
    return false
};