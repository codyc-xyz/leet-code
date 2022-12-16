# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = defaultdict(int)
        countT = collections.Counter(t)
        seen = set()
        need = len(set(t))
        minLen = float("inf")
        l = r = 0
        flag = False
        while r < len(s):
            c = s[r]
            countS[c] += 1
            if c in t and c not in seen and countS[c] >= countT[c]:
                seen.add(c)
            while len(seen) == need:
                if r - l + 1 < minLen:
                    right, left = r + 1, l
                    minLen = right - left
                    flag = True
                j = s[l]
                countS[j] -= 1
                if j in seen and countS[j] < countT[j]:
                    seen.remove(j)
                l += 1
            r += 1
        if flag == True:
            return s[left:right]
        else:
            return ""