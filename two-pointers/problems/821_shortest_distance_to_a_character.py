# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr = []
        ret = []
        n = 0
        for i in range(len(s)):
            if s[i] == c:
                arr.append(i)
        
        for i in range(len(s)):
            if n < len(arr) - 1:
                if abs(arr[n] - i) > abs(arr[n + 1] - i):
                    n += 1
            ret.append(abs(arr[n] - i))
        return ret