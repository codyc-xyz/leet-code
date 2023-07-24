# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow(curr, x, n):
            if n > 0:
                return pow(curr*x, x, n - 1)
            elif n < 0:
                return pow(curr * 1/x, x, n + 1)
            else:
                return curr
        return pow(1, x, n)
