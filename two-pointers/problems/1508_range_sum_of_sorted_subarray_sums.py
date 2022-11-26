# You are given the array nums consisting of n positive integers. 
# You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

# Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. 
# Since the answer can be a huge number return it modulo 109 + 7.

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        ans = 0
        for i in range(len(nums)):
            sums.append(nums[i])
            for j in range(i + 1, len(nums)):
                sums.append(sums[-1] + nums[j])
        sums.sort()
        while left < right:
            ans += sums[left - 1] + sums[right - 1]
            left += 1
            right -= 1
        if left == right:
            ans += sums[right - 1]
        return ans 
            