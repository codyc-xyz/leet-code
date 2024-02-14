# You are given two 0-indexed integer arrays fronts and backs of length n, where the ith card has the positive integer fronts[i] printed on the front and backs[i] printed on the back. Initially, each card is placed on a table such that the front number is facing up and the other is facing down. You may flip over any number of cards (possibly zero).

# After flipping the cards, an integer is considered good if it is facing down on some card and not facing up on any card.

# Return the minimum possible good integer after flipping the cards. If there are no good integers, return 0.

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        if fronts == backs:
            return 0

        notAns = set()
        ans = set()

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                if fronts[i] in ans:
                    ans.remove(fronts[i])
                notAns.add(fronts[i])
            else:
                if fronts[i] not in notAns:
                    ans.add(fronts[i])
                if backs[i] not in notAns:
                    ans.add(backs[i])
        return min(ans) if ans else 0

