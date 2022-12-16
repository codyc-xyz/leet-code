# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l = r = 0
        ans = []
        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()  
                
            dq.append(r)
            
            if l > dq[0]:
                dq.popleft()
                
            if (r + 1) >= k:
                ans.append(nums[dq[0]])
                l += 1
            r += 1
        return ans