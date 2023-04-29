# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

# Return the length longest chain which can be formed.

# You do not need to use up all the given intervals. You can select pairs in any order.

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        ans = 1
        pairs.sort(key = lambda x: x[1])
        prevR = pairs[0][1]
        for l, r in pairs:
            if l > prevR:
                ans += 1
                prevR = r
        return ans

