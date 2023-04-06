# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        two = three = five = 0
        while len(ugly) < n:
            while ugly[two]*2 <= ugly[-1]:
                two += 1
            while ugly[three]*3 <= ugly[-1]:
                three += 1
            while ugly[five]*5 <= ugly[-1]:
                five += 1
            ugly.append(min(ugly[two]*2, ugly[three]*3, ugly[five]*5))
        return ugly[-1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        ans = []
        seen = set()
        while len(ans) < n:
            curr = heapq.heappop(ugly)
            for i in (2, 3, 5):
                if i*curr not in seen:
                    heapq.heappush(ugly, i*curr)
                    seen.add(i*curr)
            ans.append(curr)
        return ans[-1]