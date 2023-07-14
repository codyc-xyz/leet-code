# Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

# A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        if difference == 0:
            count = collections.Counter(arr)
            return max(count.values())

        hm = defaultdict(list)

        for n in arr:
            if n not in hm:
                hm[n] = 1
            curr = n - difference
            if curr in hm:
                hm[n] = hm[curr] + 1

        return max(hm.values())
