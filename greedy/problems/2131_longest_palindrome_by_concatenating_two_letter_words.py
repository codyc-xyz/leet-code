# You are given an array of strings words. Each element of words consists of two lowercase English letters.

# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

# A palindrome is a string that reads the same forward and backward.

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = collections.Counter(words)
        ans = extras = 0
        for c in count:
            if count[c] < 1:
                continue
            rev = c[::-1]
            while count[c] > 1 and count[rev] > 1:
                ans += 4
                count[c] -= 1
                count[rev] -= 1
            if count[c] >= 1 and count[rev] >= 1 and c[0] != c[1]:
                ans += 4
                count[c] -= 1
                count[rev] -= 1
        
            if c[0] == c[1] and count[c] == 1:
                extras = 2
        return ans + extras