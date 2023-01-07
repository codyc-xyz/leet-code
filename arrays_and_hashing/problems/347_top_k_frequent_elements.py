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

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
                
        for n, c in count.items():
            freq.append([c, n])
        
        freq.sort()
        ans = []
        for i in range(len(freq) - 1, len(freq) - k - 1, -1):
            ans.append(freq[i][1])
            
        return ans