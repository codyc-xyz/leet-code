# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:
# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                count = stack.pop()
                if stack:
                    stack[-1] += max(count * 2, 1)
                else:
                    ans += max(count * 2, 1)
        return ans