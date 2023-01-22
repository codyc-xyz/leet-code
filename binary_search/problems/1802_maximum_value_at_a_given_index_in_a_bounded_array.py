# You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

# nums.length == n
# nums[i] is a positive integer where 0 <= i < n.
# abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# The sum of all the elements of nums does not exceed maxSum.
# nums[index] is maximized.

# Return nums[index] of the constructed array.

# Note that abs(x) equals x if x >= 0, and -x otherwise.

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def validArr(m):
            count = 0
            for i in range(n):
                count += max(1, m - (abs(index - i)))
            return count <= maxSum
            
        
        l, r = 1, maxSum
        ans = 0
        while l <= r:
            m = (l + r) // 2
                
            if validArr(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
            
        return ans

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        distributable = maxSum - n
        def validArr(m):
            right = max(m - index, 0)
            res = (m + right) * (m - right + 1) / 2
            left = max(m - ((n - 1) - index), 0)
            res += (m + left) * (m - left + 1) / 2
            return res - m <= distributable
        
        l, r = 1, maxSum
        while l <= r:
            m = (l + r) // 2
                
            if validArr(m):
                l = m + 1
            else:
                r = m - 1

        return l