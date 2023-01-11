# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = set(arr)
        
        for i in range(1, len(arr) + k + 1):
            if i not in nums:
                k -= 1
                if k == 0:
                    return i