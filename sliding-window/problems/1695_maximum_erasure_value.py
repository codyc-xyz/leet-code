# You are given an array of positive integers nums and want to erase a subarray containing unique elements. 
# The score you get by erasing the subarray is equal to the sum of its elements.
# Return the maximum score you can get by erasing exactly one subarray.
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, 
# that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        maxScore = score = windowStart = 0
        for windowEnd in range(len(nums)):
            score += nums[windowEnd]
            counter[nums[windowEnd]] += 1
            while windowStart < windowEnd and counter[nums[windowEnd]] > 1:
                score -= nums[windowStart]
                counter[nums[windowStart]] -= 1
                windowStart += 1
            maxScore = max(maxScore, score)
            
        return maxScore

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        windowStart = score = maxScore = 0
        for windowEnd in range(len(nums)):
            score += nums[windowEnd]
            while nums[windowEnd] in seen:
                score -= nums[windowStart]
                seen.remove(nums[windowStart])
                windowStart += 1
            seen.add(nums[windowEnd])
            maxScore = max(maxScore, score)
        return maxScore
    
    
                
                
            

