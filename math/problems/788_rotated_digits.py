# An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. For example:

# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become invalid.
# Given an integer n, return the number of good integers in the range [1, n].

class Solution:
    def rotatedDigits(self, n: int) -> int:
        goodNums = {'2', '5', '6', '9'}
        validNums = goodNums.union({'0', '1', '8'})
        ans = 0
        
        for i in range(1, n + 1):
            s = str(i)
            if all(digit in validNums for digit in s) and any(digit in goodNums for digit in s):
                ans += 1
        
        return ans
