# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endIndex = {}
        for i in range(len(s)):
            endIndex[s[i]] = i
            
        size = end = 0
        res = []
        for i in range(len(s)):
            size += 1
            end = max(end, endIndex[s[i]])
            if end == i:
                res.append(size)
                size = 0
        return res