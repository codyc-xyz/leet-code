# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        ans = []
        while k > 0:
            j = max(count, key=count.get)
            ans.append(j)
            del count[j]
            k -= 1
        return ans