# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        arr = []
        maxConsec = consec = 0
        for i, c in enumerate(nums):
            if i == 0:
                consec += 1
            else:
                if c == arr[-1] + 1:
                    consec += 1
                elif c == arr[-1]:
                    continue
                else:
                    consec = 1
            arr.append(c)
            maxConsec = max(maxConsec, consec)
        return maxConsec