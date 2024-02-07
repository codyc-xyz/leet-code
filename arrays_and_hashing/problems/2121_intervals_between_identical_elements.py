# You are given a 0-indexed array of n integers arr.

# The interval between two elements in arr is defined as the absolute difference between their indices. More formally, the interval between arr[i] and arr[j] is |i - j|.

# Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and each element in arr with the same value as arr[i].

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        inter = []

        idxs = defaultdict(list)
        for i, n in enumerate(arr):
            idxs[n].append(i)

        for i, n in enumerate(arr):
            currSum = 0
            for j in idxs[n]:
                currSum += abs(j - i)
            inter.append(currSum)
        return inter
