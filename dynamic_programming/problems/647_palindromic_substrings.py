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

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        N = len(s)
        ans = 0
        cache = {}
        def checkPali(i, j, res):
            if (i, j) in cache:
                return cache[(i, j)]
            if i > j:
                return 1
            if s[i] != s[j]:
                return 0
            res += checkPali(i+1,j-1, res)
            cache[(i, j)] = res
            return cache[(i, j)]
            

        for i in range(len(s)):
            for j in range(i, len(s)):
                ans += checkPali(i, j, 0)
        return ans

        