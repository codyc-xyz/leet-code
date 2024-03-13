'''
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        pSum = [0]

        for i in range(1, n+1):
            pSum.append(pSum[-1] + i)

        for j in range(1, len(pSum)):
            if pSum[j] == pSum[-1] - pSum[j-1]:
                return j
        return -1