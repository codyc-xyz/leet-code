# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 class Solution:
    def longestPalindrome(self, s: str) -> int:

        count = collections.Counter(s)
        seenOdd = False
        ans = 0
        for c in count:
            if count[c] % 2 and not seenOdd:
                ans += count[c]
                seenOdd = True
            elif count[c] % 2:
                ans += count[c] - 1
            else:
                ans += count[c]

        return ans

