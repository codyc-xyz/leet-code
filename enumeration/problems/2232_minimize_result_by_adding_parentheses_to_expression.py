# You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent positive integers.

# Add a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+'.

# Return expression after adding a pair of parentheses such that expression evaluates to the smallest possible value. If there are multiple answers that yield the same result, return any of them.

# The input has been generated such that the original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split('+')
        ans = "(" + expression + ')'
        minRes = int(left) + int(right)
        if len(expression) == 3:
            return ans

        for i in range(len(left)):
            for j in range(1, len(right) + 1):
                multi1 = left[:i]
                add1 = left[i:]
                add2 = right[:j]
                multi2 = right[j:]
                res = (int(multi1) if multi1 else 1) * ((int(add1) if add1 else 0) + (int(add2) if add2 else 0)) * (int(multi2) if multi2 else 1)
                if res < minRes:
                    ans = multi1 + '(' + add1 + '+' + add2 + ')' + multi2
                    minRes = res
        return ans
