# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

class Solution:
    def countVowelStrings(self, n: int) -> int:

        def recurse(n, k):
            if n == 0:
                return 1
            total = 0
            for i in range(k, 5):
                total += recurse(n - 1, i)
            return total

        return recurse(n, 0)
        