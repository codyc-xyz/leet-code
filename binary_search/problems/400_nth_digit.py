# Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

class Solution:
    def findNthDigit(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if count + len(str(i)) >= n:
                return int(str(i)[n - count - 1])
            count += len(str(i))

class Solution:
    def findNthDigit(self, n: int) -> int:
        base = digit = 1
        while n > base * digit * 9:
            n -= base * digit * 9
            digit += 1
            base *= 10
        i, j = divmod(n - 1, digit)
        return int(str(base + i)[j])