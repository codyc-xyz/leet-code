# You are given an integer array nums and two integers limit and goal. The array nums has an interesting property that abs(nums[i]) <= limit.

# Return the minimum number of elements you need to add to make the sum of the array equal to goal. The array must maintain its property that abs(nums[i]) <= limit.

# Note that abs(x) equals x if x >= 0, and -x otherwise.

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:

        currSum = sum(nums)
        ans = 0
        if goal > currSum:
            target = goal - currSum
            ans += math.ceil(target / limit)
        elif goal < currSum:
            target = currSum - goal
            ans += math.ceil(target / limit)

        return ans