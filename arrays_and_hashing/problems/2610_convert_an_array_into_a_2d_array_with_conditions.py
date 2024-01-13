# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.

# Note that the 2D array can have a different number of elements on each row.

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hm = {}
        ans = [[]]
        for n in nums:
            if n not in hm:
                ans[0].append(n)
                hm[n] = 1
            else:
                if len(ans) <= hm[n]:
                    ans.append([])
                ans[hm[n]].append(n)
                hm[n] += 1
        return ans
