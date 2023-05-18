# You are given a 0-indexed array nums consisting of n positive integers.

# The array nums is called alternating if:

# nums[i - 2] == nums[i], where 2 <= i <= n - 1.
# nums[i - 1] != nums[i], where 1 <= i <= n - 1.
# In one operation, you can choose an index i and change nums[i] into any positive integer.

# Return the minimum number of operations required to make the array alternating.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        countOdd = {}
        countEven = {}

        for i, n in enumerate(nums):
            if i % 2:
                if n in countOdd:
                    countOdd[n] += 1
                else:
                    countOdd[n] = 1
            else:
                if n in countEven:
                    countEven[n] += 1
                else:
                    countEven[n] = 1

        maxOdd = maxCountOdd = secondOdd = secondCountOdd = 0
        for c in countOdd:
            if countOdd[c] > maxCountOdd:
                secondOdd = maxOdd
                maxOdd = c
                secondCountOdd = maxCountOdd
                maxCountOdd = countOdd[c]
            elif countOdd[c] > secondCountOdd:
                secondOdd = c
                secondCountOdd = countOdd[c]
    
        maxEven = maxCountEven = secondEven = secondCountEven = 0
        for c in countEven:
            if countEven[c] > maxCountEven:
                secondEven = maxEven
                maxEven = c
                secondCountEven = maxCountEven
                maxCountEven = countEven[c]
            elif countEven[c] > secondCountEven:
                secondEven = c
                secondCountEven = countEven[c]

        if maxOdd == maxEven:
            if secondCountOdd or secondCountEven:
                if secondCountOdd and secondCountEven:
                    if maxCountOdd - secondCountOdd > maxCountEven - secondCountEven:
                        maxEven = secondEven
                        maxCountEven = secondCountEven
                    else:
                        maxOdd = secondOdd
                        maxCountOdd = secondCountOdd
                elif secondCountOdd:
                    maxCountOdd = secondCountOdd
                    maxOdd = secondOdd
                elif secondCountEven:
                    maxCountEven = secondCountEven
                    maxEven = secondEven
            else:
                return len(nums) // 2
        return len(nums) - (maxCountOdd + maxCountEven)