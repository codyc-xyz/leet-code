# You are given a 0-indexed integer array nums whose length is a power of 2.

# Apply the following algorithm on nums:

# Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
# For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
# For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
# Replace the array nums with newNums.
# Repeat the entire process starting from step 1.
# Return the last number that remains in nums after applying the algorithm.

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        N = len(nums)
        while N > 1:
            newNums = []
            for i in range(len(nums) // 2):
                if not i % 2:
                    newNums.append(min(nums[2*i], nums[2*i+1]))
                else:
                    newNums.append(max(nums[2*i], nums[2*i+1]))
            nums = newNums
            N = len(nums)
        return nums[0]