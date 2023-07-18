# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0

        for i in range(N):
            for j in range(i, N):
                curr = s[i:j+1]
                if curr == curr[::-1]:
                    ans += 1
        return ans
