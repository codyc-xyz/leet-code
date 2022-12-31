# We are given hours, a list of the number of hours worked per day for a given employee.

# A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

# A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

# Return the length of the longest well-performing interval.

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        interval = 0
        psum = [0]
        seen = {}
        
        for i, n in enumerate(hours):
        
            if n > 8:
                psum.append(psum[-1] + 1)
            else:
                psum.append(psum[-1] - 1)
            
        for i, n in enumerate(psum):
            if n > 0:
                interval = max(interval, i)
            if n not in seen:
                seen[n] = i
            if n - 1 in seen:
                interval = max(interval, i - seen[n - 1])
                
        return interval