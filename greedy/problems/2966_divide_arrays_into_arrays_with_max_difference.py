# You are given an integer array nums of size n and a positive integer k.

# Divide the array into one or more arrays of size 3 satisfying the following conditions:

# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        i = 0
        prev = None
        for n in nums:
            if len(ans[i]) > 2:
                ans.append([])
                i += 1
                prev = None
            if prev and n > prev + k:
                return []
            ans[i].append(n)
            if len(ans[i]) == 1:
                prev = n

        return ans