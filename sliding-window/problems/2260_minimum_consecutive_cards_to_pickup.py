# You are given an integer array cards where cards[i] represents the value of the ith card. 
# A pair of cards are matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. 
# If it is impossible to have matching cards, return -1.

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hm = {}
        diff, minDiff = 0, float("inf")
        for i, c in enumerate(cards):
            if c in hm:
                diff = i - hm[c] + 1
                minDiff = min(minDiff, diff)
            hm[c] = i
        if diff != 0:
             return minDiff 
        else:
            return -1