// You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

// Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

// Note:

// The frequency of a letter x is the number of times it occurs in the string.
// You must remove exactly one letter and cannot choose to do nothing.

function equalFrequency(word: string): boolean {

    let res: number[] = new Array(26).fill(0);
    for (let i = 0; i < word.length; i++) {
        let idx: number = word[i].charCodeAt(0) - 'a'.charCodeAt(0);
        res[idx] += 1
    }

    for (let i = 0; i < res.length; i++) {
        if (res[i] > 0) {
            res[i] -= 1
            let set = new Set(res)
            set.delete(0)
            if (set.size === 1) {
                return true
            }
            res[i] += 1
        }
    }
    return false
}