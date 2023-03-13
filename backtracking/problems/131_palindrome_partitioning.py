# Given a string s, partition s such that every substring of the partition is a palindrome. 
# Return all possible palindrome partitioning of s.

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        part = []
        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            if i >= len(s):
                ans.append(part[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i:j + 1]):
                    part.append(s[i:j + 1])
                    backtrack(j + 1)
                    part.pop()
        backtrack(0)
        return ans