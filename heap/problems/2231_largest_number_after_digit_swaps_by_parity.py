# You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

# Return the largest possible value of num after any number of swaps.

class Solution:
    def largestInteger(self, num: int) -> int:
        nums = str(num)
        odds = []
        evens = []
        for n in nums:
            if int(n) % 2:
                odds.append(int(n) * -1)
            else:
                evens.append(int(n) * -1)

        heapq.heapify(odds)
        heapq.heapify(evens)
        ans = ""
        for n in nums:
            if int(n) % 2:
                ans = ans + str(heapq.heappop(odds) * -1)
            else:
                ans = ans + str(heapq.heappop(evens) * -1)

        return int(ans)