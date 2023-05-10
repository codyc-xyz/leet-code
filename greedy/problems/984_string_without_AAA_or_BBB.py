# Given two integers a and b, return any string s such that:

# s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
# The substring 'aaa' does not occur in s, and
# The substring 'bbb' does not occur in s.

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ""
        while a > 0 or b > 0:
            if (a >= b and not ans) or (a >= b and ans[-1] != 'a') or (ans and ans[-1] == 'b'):
                if a > 1 and (not b or a / b > 2/3):
                    ans += 'aa'
                    a -= 2
                else:
                    ans += 'a'
                    a -= 1
            else:
                if b > 1 and (not a or b / a > 2/3):
                    ans += 'bb' 
                    b -= 2
                else:
                    ans += 'b'
                    b -= 1
        return ans
