# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.

class Solution:
    def findLucky(self, arr: List[int]) -> int:

        count = collections.Counter(arr)
        ans = []
        for c in sorted(count, reverse=True):
            if c == count[c]:
                return c
        return -1
        
        