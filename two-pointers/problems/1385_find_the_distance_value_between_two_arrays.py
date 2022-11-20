# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in range(len(arr1)):
            count = 0
            for n in range(len(arr2)):
                if abs(arr1[i] - arr2[n]) <= d:
                    count += 1
                    break
            if count == 0:
                ans += 1
        return ans