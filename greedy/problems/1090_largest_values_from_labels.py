# There is a set of n items. You are given two integer arrays values and labels where the value and the label of the ith element are values[i] and labels[i] respectively. You are also given two integers numWanted and useLimit.

# Choose a subset s of the n elements such that:

# The size of the subset s is less than or equal to numWanted.
# There are at most useLimit items with the same label in s.
# The score of a subset is the sum of the values in the subset.

# Return the maximum score of a subset s.

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:

        heap = [[-v, l] for v, l in zip(values, labels)]
        heapq.heapify(heap)
        taken = ans = 0
        hm = {}

        while heap and taken < numWanted:
            value, label = heapq.heappop(heap)
            if label not in hm:
                hm[label] = 1
                ans -= value
                taken += 1
            elif hm[label] < useLimit:
                hm[label] += 1
                ans -= value
                taken += 1
        return ans

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:

        arr = [[v, l] for v, l in zip(values, labels)]
        arr.sort(reverse=True)
        taken = ans = 0
        hm = {}

        for value, label in arr:
            if taken == numWanted:
                break
            if label not in hm:
                hm[label] = 1
                ans += value
                taken += 1
            elif hm[label] < useLimit:
                hm[label] += 1
                ans += value
                taken += 1
        return ans