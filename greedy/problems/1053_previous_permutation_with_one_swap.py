# Given an array of positive integers arr (not necessarily distinct), return the lexicographically
# largest permutation that is smaller than arr, that can be made with exactly one swap. If it cannot be done, then return the same array.
# Note that a swap exchanges the positions of two numbers arr[i] and arr[j]

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
        if i < 0:
            return arr
        j = n - 1
        while arr[j] >= arr[i]:
            j -= 1
        while j > i and arr[j-1] == arr[j]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        return arr
