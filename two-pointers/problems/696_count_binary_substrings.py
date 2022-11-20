# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, 
# and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        arr = [1]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                arr[-1] += 1
            else:
                arr.append(1)
        for i in range(1, len(arr)):
            ans += min(arr[i], arr[i - 1])
        return ans