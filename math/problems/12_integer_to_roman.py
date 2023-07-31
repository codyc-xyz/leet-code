# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# 
# I can be placed before V(5) and X(10) to make 4 and 9.
# X can be placed before L(50) and C(100) to make 40 and 90.
# C can be placed before D(500) and M(1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

class Solution:
    def intToRoman(self, num: int) -> str:

        digits = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV',
                  '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
        i = ans = 0

        NUM = str(num)
        N = len(NUM)
        ans = ""
        while i < N:
            if N - i > 3:
                ans += int(NUM[i]) * 'M'
            elif N - i > 2:
                if NUM[i] == '9':
                    ans += 'CM'
                elif NUM[i] == '4':
                    ans += 'CD'
                elif int(NUM[i]) >= 5:
                    hundreds = int(NUM[i]) - 5
                    ans += 'D'

                    if hundreds:
                        ans += 'C' * int(hundreds)
                else:
                    ans += 'C' * int(NUM[i])
            elif N - i > 1:
                if NUM[i] == '9':
                    ans += 'XC'
                elif NUM[i] == '4':
                    ans += 'XL'
                elif int(NUM[i]) >= 5:
                    tens = int(NUM[i]) - 5
                    ans += 'L'
                    if tens:
                        ans += 'X' * int(tens)
                else:
                    ans += int(NUM[i]) * 'X'
            else:
                if NUM[i] != '0':
                    ans += digits[NUM[i]]
            i += 1

        return ans
