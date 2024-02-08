# You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the maximum digit in both numbers are equal.

# Return the maximum sum or -1 if no such pair exists.

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        maxDigit = defaultdict(list)

        for n in nums:
            N = str(n)
            maxNum = max(int(c) for c in N)
            maxDigit[maxNum].append(n)

        for k in maxDigit:
            maxDigit[k].sort(reverse=True)
        ans = -1
        for k in maxDigit:
            if len(maxDigit[k]) > 1:
                ans = max(ans, maxDigit[k][0] + maxDigit[k][1])
        return ans
