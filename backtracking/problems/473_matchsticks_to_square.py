# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. 
# You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total = sum(matchsticks)
        
        if total % 4:
            return False
        self.target = total // 4
        used = [False] * len(matchsticks)
        buckets = [0] * 4
        def backtrack(i, sides):
            if sides == 4:
                return True
            
            for j in range(i, len(matchsticks)):
                if not used[j]:
                    for x, b in enumerate(buckets):
                        if b + matchsticks[j] == self.target:
                            buckets[x] += matchsticks[j]
                            used[j] = True
                            sides += 1
                            if backtrack(j + 1, sides):
                                return True
                            used[j] = False
                            buckets[x] -= matchsticks[j]
                            sides -= 1
                        elif b + matchsticks[j] < self.target:
                            buckets[x] += matchsticks[j]
                            used[j] = True
                            if backtrack(j + 1, sides):
                                return True
                            buckets[x] -= matchsticks[j]
                            used[j] = False
            return False
        return backtrack(0, 0)