# There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. 
# After that, the teacher will restart the process, starting with the student number 0 again.

# You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. 
# However, if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be asked to replace the chalk.

# Return the index of the student that will replace the chalk.

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        pSum = [chalk[0]]
        
        for i in range(1, len(chalk)):
            pSum.append(pSum[-1] + chalk[i])
     
        l, r = 0, 10**9
        while l < r:
            m = (l + r) // 2
            if  pSum[-1] * m <= k:
                multi = m
                l = m + 1
            else:
                r = m
        res = pSum[-1] * multi

        l, r = 0, len(chalk) - 1
        while l < r:
            m = (l + r) // 2
            
            if res + pSum[m] <= k:
                l = m + 1
            else:
                r = m
        return l