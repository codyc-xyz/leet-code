# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = ""
        num = str(num)
        flag = False
        for i, n in enumerate(num):
            if n == '6' and flag == False:
               ans +=  '9'
               flag = True
            else:
                ans += n
        return int(ans)