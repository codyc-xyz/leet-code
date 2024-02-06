# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False
        while not n % 2:
            n //= 2
        while not n % 3:
            n //= 3
        while not n % 5:
            n //= 5
        return n == 1