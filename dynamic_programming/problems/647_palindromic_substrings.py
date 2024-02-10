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


class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0

        for i in range(N):
            l = r = i
            while l >= 0 and r < N and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        N = len(s)
        ans = len(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    ans += 1       
        return ans 

