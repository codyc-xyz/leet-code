# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

# Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        targetSum = sum(arr) // 3 
        partitions = currSum = j = 0
        while j < len(arr):
            currSum += arr[j]
            if currSum == targetSum and (partitions < 2 or j == len(arr) - 1):
                partitions += 1
                currSum = 0
            j += 1
        if partitions == 3 and not currSum:
            return True
        return False
