# You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:
# m is greater than 1.
# s1 = s0 + 1.
# The 0-indexed subarray s looks like[s0, s1, s0, s1, ..., s(m-1) % 2]. In other words, s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1, and so on up to s[m - 1] - s[m - 2] = (-1)m.
# Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:

        N = len(nums)
        if N <= 1:
            return -1
        maxLen = -1
        i, j = 0, 1
        while j < N:
            start = i
            if nums[i] + 1 != nums[j]:
                i += 1
                j += 1
                continue
            curr = nxt = 1
            while j < N:
                if nums[i] + nxt == nums[j]:
                    j += 1
                    i += 1
                    nxt *= -1
                    curr += 1
                else:
                    break
            i = start + 1
            j = i + 1
            maxLen = max(maxLen, curr)
        return maxLen
