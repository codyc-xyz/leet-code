# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9+7
        N = len(s)
        consecOnes = [0]
        for c in s:
            if c == '1':
                consecOnes.append(consecOnes[-1] + 1)
            else:
                consecOnes.append(0)
        return sum(consecOnes) % MOD