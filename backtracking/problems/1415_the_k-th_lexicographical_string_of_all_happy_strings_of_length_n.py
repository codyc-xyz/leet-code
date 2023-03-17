# A happy string is a string that: consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

# Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

class Solution:
    def getHappyString(self, n: int, k: int) -> str:


        happy = []

        def backtrack(i, curr):
            if len(happy) >= k:
                return
            if i == n:
                happy.append(curr)
                return
            if not curr or curr[-1] != 'a':
                backtrack(i + 1, curr + 'a')
            if not curr or curr[-1] != 'b':
                backtrack(i + 1, curr + 'b')
            if not curr or curr[-1] != 'c':
                backtrack(i + 1, curr + 'c')

        backtrack(0, "")
        if len(happy) >= k:
            return happy[-1]
        else:
            return ""