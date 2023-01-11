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

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] - k - 1 < mid:
                l = mid + 1
            else:
                r = mid - 1
        return l + k