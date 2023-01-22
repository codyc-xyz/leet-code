# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        n = len(potions)
        
        for s in spells:
            l, r = 0, n
            res = -1
            while l <= r:
                m = (l + r) // 2
                if m >= n:
                    break
                if potions[m] * s >= success:
                    r = m - 1
                    res = m
                else:
                    l = m + 1
            if res != -1:
                ans.append(n - res)
            else:
                ans.append(0)
        return ans