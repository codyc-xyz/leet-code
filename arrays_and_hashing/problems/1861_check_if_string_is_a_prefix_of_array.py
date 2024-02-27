# Given a string s and an array of strings words, determine whether s is a prefix string of words.

# A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

# Return true if s is a prefix string of words, or false otherwise.

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res = ""

        for w in words:
            res += w
            if len(res) > len(s):
                return False
            if res == s:
                return True
        return False