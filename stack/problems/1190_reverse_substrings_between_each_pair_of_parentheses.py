# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

class Solution:
    def reverseParentheses(self, s: str) -> str:
            
        stack = []

        for n in s:
            if n != ')':
                stack.append(n)
            else:
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                stack += tmp
        return "".join(stack)