# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].

# Given a string s, reconstruct the permutation perm and return it. 
# If there are multiple valid permutations perm, return any of them.

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        ans = []
        for i in range(len(s)):
            if s[i] == 'I':
                ans.append(low)
                low += 1
                if i == len(s) - 1:
                    ans.append(high)
            else:
                ans.append(high)
                high -= 1
                if i == len(s) - 1:
                    ans.append(low)
        return ans