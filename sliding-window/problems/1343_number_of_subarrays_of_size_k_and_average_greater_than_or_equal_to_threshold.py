# Given an array of integers arr and two integers k and threshold, 
# return the number of sub-arrays of size k and average greater than or equal to threshold.

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        for n in range(len(arr)):
            for i in range(len(arr) - k + 1):
                sub = arr[n:i+k]
                if len(sub) != k:
                    continue
                if (sum(sub) / k) >= threshold:
                    count += 1
        return count