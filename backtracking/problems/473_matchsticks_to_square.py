# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. 
# You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
     
        total = sum(matchsticks)
        if total % 4:
            return False
        matchsticks.sort(reverse=True)
        self.target = total // 4
        buckets = [0] * 4
        def backtrack(i):
            if i == len(matchsticks):
                return True
            for j, b in enumerate(buckets):
                if b + matchsticks[i] <= self.target:
                    buckets[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    buckets[j] -= matchsticks[i]
            return False
        return backtrack(0)