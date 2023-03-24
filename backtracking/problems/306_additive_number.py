# An additive number is a string whose digits can form an additive sequence.

# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

# Given a string containing only digits, return true if it is an additive number or false otherwise.

# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)
        def backtrack(i, seq, curr):
            if len(seq) > 2 and seq[-3] + seq[-2] != seq[-1] or (len(curr) > 1 and curr[0] == '0'):
                return False
            if i == len(num):
                currLen = 0
                for i in range(len(seq)):
                    currLen += len(str(seq[i]))

                return len(seq) > 2 and currLen == N
            
            
            return backtrack(i + 1, seq, curr + num[i]) or backtrack(i + 1, seq + [int(curr + num[i])], "")

        for i in range(N):
            
            if backtrack(i + 1, [int(num[:i + 1])], ""):
                return True
        return False