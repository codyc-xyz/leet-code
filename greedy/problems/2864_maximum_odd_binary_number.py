'''
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.
'''

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = collections.Counter(s)
        ans = ""
        for i in range(len(s)-1):
            if count['1'] > 1:
                ans += '1'
                count['1'] -= 1
            else:
                ans += '0'
        return ans + '1'