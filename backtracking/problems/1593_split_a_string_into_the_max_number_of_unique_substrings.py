# Given a string s, return the maximum number of unique substrings that the given string can be split into.

# You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

# A substring is a contiguous sequence of characters within a string.

class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        self.ans = 0
        def backtrack(path, i):
            if i >= len(s):
                self.ans = max(self.ans, len(path))
                return

            for j in range(i+1, len(s)+1):
                if s[i:j] not in path:
                    path.add(s[i:j])
                    backtrack(path, j)
                    path.remove(s[i:j])

        backtrack(set(), 0)
        return self.ans