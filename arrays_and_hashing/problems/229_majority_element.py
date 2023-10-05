# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        lenNums = len(nums)
        target = lenNums / 3
        count = collections.Counter(nums)

        ans = []

        for c in count:
            if count[c] > target:
                ans.append(c)

        return ans
