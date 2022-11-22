# Given an array arr of integers, check if there exist two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hm = {}
        
        for i in range(len(arr)):
            if arr[i] * 2 in hm or arr[i] / 2 in hm:
                return True
            hm[arr[i]] = i
        return False