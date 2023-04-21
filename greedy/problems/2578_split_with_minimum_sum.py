# Given a positive integer num, split it into two non-negative integers num1 and num2 such that:

# The concatenation of num1 and num2 is a permutation of num.
# In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
# num1 and num2 can contain leading zeros.
# Return the minimum possible sum of num1 and num2.

# Notes:

# It is guaranteed that num does not contain any leading zeros.
# The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.

class Solution:
    def splitNum(self, num: int) -> int:
        nums = sorted(str(num))
        n1, n2 = "", ""
        for i, n in enumerate(nums):
            if not i % 2:
                n1 += n
            else:
                n2 += n
        return int(n1) + int(n2)

