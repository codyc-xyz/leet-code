# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

class Solution:

    def __init__(self, w: List[int]):
        self.sumW = sum(w)
        self.prob = [w[0]]
        for i in range(1, len(w)):
            self.prob.append(self.prob[-1] + w[i])
        
    def pickIndex(self) -> int:
        i = randint(1, self.sumW)
        l, r = 0, len(self.prob) - 1
        
        while l < r:
            m = (l + r) // 2
            if self.prob[m] < i:
                l = m + 1
            else:
                r = m
        return l