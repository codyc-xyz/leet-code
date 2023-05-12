# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        arrDict = defaultdict(list)

        for i, n in enumerate(nums):
            for a in arrDict:
                if n > arrDict[a][-1]:
                    arrDict[a].append(n)
                    if len(arrDict[a]) == 3:
                        return True
                elif n < arrDict[a][-1] and n > min(arrDict[a]):
                    arrDict[a].pop()
                    arrDict[a].append(n)
            arrDict[i].append(n)
        return False