# You are given an integer array cards where cards[i] represents the value of the ith card. 
# A pair of cards are matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. 
# If it is impossible to have matching cards, return -1.

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hm = {}
        minConsec = float("inf")
        for windowEnd, card in enumerate(cards):
            if card in hm:
                minConsec = min(minConsec, windowEnd - hm[card] + 1)
            hm[card] = windowEnd
        if minConsec != float("inf"):
            return minConsec
        else:
            return -1