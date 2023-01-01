# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        if len(num) <= k:
            return '0'
        
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            if int(n) or stack:
                stack.append(n)
        if k:
            stack = stack[:-k]
        if stack:
            return "".join(stack)
        else:
            return '0'