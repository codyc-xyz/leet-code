# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = [None] * len(spells) 
        potions.sort()
        
        for i, n in enumerate(spells):
            r = len(potions) - 1
            while r >= 0:
                if potions[r] * n < success:
                    pairs[i] = len(potions) - r - 1
                    break
                elif r == 0:
                    pairs[i] = len(potions)
                    break
                r -= 1
        return pairs