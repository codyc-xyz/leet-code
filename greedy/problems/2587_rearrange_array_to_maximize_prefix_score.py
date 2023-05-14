# You are given a 0-indexed integer array nums. You can rearrange the elements of nums to any order (including the given order).

# Let prefix be the array containing the prefix sums of nums after rearranging it. In other words, prefix[i] is the sum of the elements from 0 to i in nums after rearranging it. The score of nums is the number of positive integers in the array prefix.

# Return the maximum score you can achieve.

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ans = 0
        nums.sort(reverse = True)
        currSum = 0
        for n in nums:
            currSum += n
            if currSum > 0:
                ans += 1
            else:
                break
        return ans 