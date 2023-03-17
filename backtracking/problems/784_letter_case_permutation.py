# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        ans = set()

        def backtrack(i, curr):
            if i == len(s):
                ans.add(curr)
                return
            if s[i].isdigit():
                backtrack(i + 1, curr + s[i])
            else:
                backtrack(i + 1, curr + s[i].lower())
                backtrack(i + 1, curr + s[i].upper())
        backtrack(0, "")
        return ans