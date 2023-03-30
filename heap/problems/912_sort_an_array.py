# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       
        heapq.heapify(nums)
        ans = []

        while nums:
            ans.append(heapq.heappop(nums))

        return ans
