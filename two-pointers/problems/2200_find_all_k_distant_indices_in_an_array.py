# You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

# Return a list of all k-distant indices sorted in increasing order.

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        ans = set()
        l = 0
        for i, n in enumerate(nums):
            if i - l > k:
                l += 1
            if n == key:
                for j in range(l, i + k + 1):
                    if j == len(nums):
                        break
                    ans.add(j)
        return list(ans)
