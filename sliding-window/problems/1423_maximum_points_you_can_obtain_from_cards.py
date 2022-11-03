# There are several cards arranged in a row, and each card has an associated number of points. 
# The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. 
# You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        currSum = sum(cardPoints[k:])
        ans = total - currSum
        
        for i in range(1, k + 1):
            currSum += cardPoints[k - i] - cardPoints[len(cardPoints) - i]
            ans = max(ans, total - currSum)
        return ans
            



