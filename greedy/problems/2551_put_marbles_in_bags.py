# You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

# Divide the marbles into the k bags according to the following rules:

# No bag is empty.
# If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
# If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
# The score after distributing the marbles is the sum of the costs of all the k bags.

# Return the difference between the maximum and minimum scores among marble distributions.

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        N = len(weights)
        adj = []
        for i in range(1, N):
            adj.append(weights[i] + weights[i - 1])

        adj.sort()
        cutsMax = cutsMin = k - 1
        minW = weights[0] + weights[-1]
        maxW = weights[0] + weights[-1]
        for w in adj:
            if cutsMin == 0:
                break
            minW += w
            cutsMin -= 1

        for w in adj[::-1]:
            if cutsMax == 0:
                break
            maxW += w
            cutsMax -= 1

        return maxW - minW
