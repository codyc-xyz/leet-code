# The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

# if x is even then x = x / 2
# if x is odd then x = 3 * x + 1
# For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

# Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

# Return the kth integer in the range [lo, hi] sorted by the power value.

# Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1 using these steps and that the power of x is will fit in a 32-bit signed integer.

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        hm = {1: 0}

        for i in range(lo, hi + 1):
            curr = i
            steps = 0
            while curr not in hm:
                if curr % 2:
                    curr *= 3
                    curr += 1
                else:
                    curr /= 2
                steps += 1
            hm[i] = steps + hm[curr]
        heap = []
        if lo > 1:
            del hm[1]
            
        for val in hm:
            heapq.heappush(heap, [hm[val], val])

        while k > 0:
            _, ans = heapq.heappop(heap)
            k -= 1
        return ans

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        hm = {1: 0}

        def getPower(curr):
            if curr not in hm:
                if curr % 2:
                    hm[curr] = 1 + getPower(curr * 3 + 1)
                else:
                    hm[curr] = 1 + getPower(curr // 2)
            return hm[curr]
            
        arr = []
        for i in range(lo, hi + 1):
            hm[i] = getPower(i)
            arr.append([hm[i], i])

        arr.sort()
        return arr[k - 1][1]