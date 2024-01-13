# Assume you are an awesome parent and want to give your children some cookies. 
# But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. 
# If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
# Your goal is to maximize the number of your content children and output the maximum number.

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sortGreed = sorted(g)
        sortSize = sorted(s)
        length = max(len(g), len(s))
        a = b = 0
        for i in range(length):
            if a >= len(g) or b >= len(s):
                break
            if sortGreed[a] <= sortSize[b]:
                a += 1
            b += 1
        return a
    

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        G = sorted(g)
        S = sorted(s)
        ans = j = 0
        for i in range(len(s)):
            if j >= len(g):
                return ans
            if S[i] >= G[j]:
                j += 1
                ans += 1
        return ans
