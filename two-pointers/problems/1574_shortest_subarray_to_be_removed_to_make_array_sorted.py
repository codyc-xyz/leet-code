# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

# Return the length of the shortest subarray to remove.

# A subarray is a contiguous subsequence of the array.

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        left, right = 0, len(arr) - 1
        
        while right - 1 >= 0 and arr[right - 1] <= arr[right]:
            right -= 1
            
        while left + 1 < len(arr) and arr[left + 1] >= arr[left]:
            left += 1
        
        if left == len(arr) - 1:
            return 0
        
        remove = min(len(arr) - left - 1, right)
        
        for i in range(left + 1):
            while right < len(arr) and arr[i] > arr[right]:
                right += 1
            if right == len(arr):
                break
            remove = min(remove, right - i - 1)
            
        return remove