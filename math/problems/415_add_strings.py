# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        l1, l2 = len(num1) - 1, len(num2) - 1
        x, carry = 0, 0
        ans = deque()

        while l1 >= 0 or l2 >= 0 or carry > 0:
            digit1 = int(num1[l1]) if l1 >= 0 else 0
            digit2 = int(num2[l2]) if l2 >= 0 else 0

            x = digit1 + digit2 + carry
            carry = x // 10
            x %= 10
            ans.appendleft(str(x))
            if l1 >= 0:
                l1 -= 1
            if l2 >= 0:
                l2 -= 1
        return ''.join(ans)
