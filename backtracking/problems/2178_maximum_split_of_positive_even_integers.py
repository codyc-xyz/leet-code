# You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.

# For example, given finalSum = 12, the following splits are valid (unique positive even integers summing up to finalSum): (12), (2 + 10), (2 + 4 + 6), and (4 + 8). 
# Among them, (2 + 4 + 6) contains the maximum number of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.
# Return a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for finalSum, return an empty list. You may return the integers in any order.

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        num = 2
        currSum = 0
        ans = []

        while currSum + num + num <= finalSum - 2:
            currSum += num
            ans.append(num)
            num += 2
        if currSum < finalSum:
            ans.append(finalSum - currSum)
        return ans               