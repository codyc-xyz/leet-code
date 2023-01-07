# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        ans = []
        while k > 0:
            ans.append(max(count, key=count.get))
            del count[max(count, key=count.get)]
            k -= 1
        return ans