# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in an ascending order, return compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

# If there are several possible values for h, the maximum one is taken as the h-index.

# You must write an algorithm that runs in logarithmic time.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def isValid(m):
            h = bisect_left(citations, m)
            if len(citations) - h >= m:
                return True
            return False
        

        l, r = 0, citations[-1]
        
        while l <= r:
            m = (l + r) // 2
            if isValid(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans