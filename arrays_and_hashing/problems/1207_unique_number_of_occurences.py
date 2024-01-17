# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        seen = set()
        for c in count:
            if count[c] in seen:
                return False
            seen.add(count[c])
        return True
