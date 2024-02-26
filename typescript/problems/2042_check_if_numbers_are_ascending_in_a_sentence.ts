// A sentence is a list of tokens separated by a single space with no leading or trailing spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.

// For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other tokens such as "puppy" are words.
// Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).

// Return true if so, or false otherwise.

function areNumbersAscending(s: string): boolean {
    let prev: number = -Infinity;

    for (let i = 0; i < s.length; i++) {
        let curr: string = ""
        while (i < s.length && !isNaN(Number(s[i])) && s[i] !== " ") {            
            curr += s[i]
            i += 1
        }
        if (curr != "") {
            const res: number = Number(curr);
            if (res <= prev) {
                return false
            }
            else {
                prev = res
            }
        }
    }
    return true
};