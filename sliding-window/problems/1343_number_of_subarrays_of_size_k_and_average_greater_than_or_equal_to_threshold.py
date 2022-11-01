# Given an array of integers arr and two integers k and threshold, 
# return the number of sub-arrays of size k and average greater than or equal to threshold.

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = sum(arr[:k])
        if res / k >= threshold:
            count = 1
        else:
            count = 0
        for n in range(len(arr) - k):
            res -= arr[n]
            res += arr[n + k]
            if res / k >= threshold:
                count += 1
         
        return count