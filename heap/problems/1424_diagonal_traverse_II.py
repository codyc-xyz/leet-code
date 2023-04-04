# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)
        heap = defaultdict(list)
        for i in range(rows):
            for j in range(len(nums[i])):
                heapq.heappush(heap[i + j], [j, nums[i][j]])

        ans = []
        for h in heap:
            while heap[h]:
                ans.append(heapq.heappop(heap[h])[1])
         
        return ans

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)
        heap = []
        for i in range(rows):
            for j in range(len(nums[i])):
                heapq.heappush(heap, [i + j, j, nums[i][j]])

        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[2])
         
        return ans

            

