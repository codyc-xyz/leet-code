# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for n in nums:
            if n in hm:
                hm[n] += 1
                if hm[n] > len(nums) / 2:
                    return n
            else:
                hm[n] = 1
        return max(hm, key=hm.get) 
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        return max(count, key=count.get)