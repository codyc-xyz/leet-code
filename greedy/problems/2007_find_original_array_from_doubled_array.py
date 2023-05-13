# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        changed.sort()
        hm = {}
        ans = []
        for c in changed:
            if not hm or (c % 2) or (not c % 2 and c // 2 not in hm):
                if c in hm:
                    hm[c] += 1
                else:
                    hm[c] = 1
                continue
            orig = c//2
            if hm[orig] > 0:
                hm[orig] -= 1
                if hm[orig] == 0:
                    del hm[orig]
                ans.append(orig)
            else:
                return []
        return [] if hm else ans
