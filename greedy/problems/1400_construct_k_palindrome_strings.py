# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        count = collections.Counter(s)
        odds = 0
        for c in count:
            if count[c] % 2:
                odds += 1
        return odds <= k