# You are given a string num consisting of digits only.

# Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

# Notes:

# You do not need to use all the digits of num, but you must use at least one digit.
# The digits can be reordered.

class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = collections.Counter()
        biggestOdd = float('-inf')
        for c in num:
            count[c] += 1

        heap = []
        for c in count:
            if count[c] % 2:
                biggestOdd = max(biggestOdd, int(c))
        if biggestOdd != float('-inf'):
            ans = str(biggestOdd)
            count[ans] -= 1
        else:
            ans = ""
        for c in count:
            if not count[c] % 2 and count[c] > 0:
                heapq.heappush(heap, [int(c), count[c]])
            elif count[c] % 2 and count[c] > 2:
                heapq.heappush(heap, [int(c), count[c] - 1])

        while heap:
            n, count = heapq.heappop(heap)
            if n == 0 and not heap:
                break
            n = str(n)
            ans = (n * (count // 2)) + ans + (n * (count // 2))
        return ans if ans else "0"

