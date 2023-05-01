# You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

# In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

# Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)

        i, j = 1, 6

        sum1, sum2 = sum(nums1), sum(nums2)
        ans = 0

        if sum1 < sum2:
            target = sum2 - sum1
            while (i < 6 or j > 0) and target > 0:
                if i - 1 <= 6 - j:
                    if count1[i] > 0:
                        count1[i] -=1
                        target -= 6 - i
                        ans += 1
                    else:
                        i += 1
                else:
                    if count2[j] > 0:
                        count2[j] -= 1
                        target -= j - 1
                        ans += 1
                    else:
                        j -= 1
        elif sum1 > sum2:
            target = sum1 - sum2
            while (i < 6 or j > 0) and target > 0:
                if i - 1 <= 6 - j:
                    if count2[i] > 0:
                        count2[i] -=1
                        target -= 6 - i
                        ans += 1
                    else:
                        i += 1
                else:
                    if count1[j] > 0:
                        count1[j] -= 1
                        target -= j - 1
                        ans += 1
                    else:
                        j -= 1
        return ans if i < 6 or j > 0 else -1
                