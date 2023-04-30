# You are given a 0-indexed array of distinct integers nums.

# There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.

# A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

# Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        maxIdx, minIdx = nums.index(max(nums)), nums.index(min(nums))

        l, r = 0, len(nums) - 1
        ans = 0
        closestTo0 = min(maxIdx, minIdx)
        closestToLen = r - max(minIdx, maxIdx)
        if closestTo0 < closestToLen:
            l = closestTo0
            ans = closestTo0 + 1
            last = max(minIdx, maxIdx)
            ans += min(abs(last - l), abs(r - last + 1)) 
        else:
            r = max(minIdx, maxIdx)
            ans = closestToLen + 1
            ans += min(abs(closestTo0 - l + 1), abs(r - closestTo0)) 
        return ans



