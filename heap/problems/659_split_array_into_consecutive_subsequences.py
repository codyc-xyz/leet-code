# You are given an integer array nums that is sorted in non-decreasing order.

# Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
# All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.

# A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. 
# (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        subseqs = [[]]
        j = 0
        for n in nums:
            if not subseqs[j] or n == subseqs[j][-1] + 1:
                subseqs[j].append(n)
            else:
                flag = False
                for i in range(len(subseqs) -2, -1, -1):
                    if n == subseqs[i][-1] +1:
                        subseqs[i].append(n)
                        flag = True
                        break
                if not flag:
                    subseqs.append([n])
                    j += 1
        for s in subseqs:
            if len(s) < 3:
                return False
        return True
