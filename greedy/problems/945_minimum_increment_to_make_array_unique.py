# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

# Return the minimum number of moves to make every value in nums unique.

# The test cases are generated so that the answer fits in a 32-bit integer.

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        count = collections.Counter(nums)
        ans = 0
        res = set()
        arr = [[c, count[c]] for c in count]
        arr.sort(reverse=True)
        for c, count in arr:
            for _ in range(count):
                if c not in res:
                    res.add(c)
                else:
                    curr = c
                    while curr in res:
                        curr += 1
                        ans += 1
                    res.add(curr)
        return ans