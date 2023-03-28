# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = [s * -1 for s in score]

        heapq.heapify(scores)
        ans = [None] * len(score)
        hm = {}
        for i, s in enumerate(score):
            hm[s * -1] = i
            
        i = 0
        while scores:
            curr = heapq.heappop(scores)
            if i > 2:
                ans[hm[curr]] = str(i + 1) 
            elif i == 2:
                ans[hm[curr]] = "Bronze Medal"
            elif i == 1:
                ans[hm[curr]] = "Silver Medal"
            elif i == 0:
                ans[hm[curr]] = "Gold Medal"
            i += 1
        return ans
        
        
