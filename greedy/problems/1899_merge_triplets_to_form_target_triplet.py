# A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

# To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

# Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
# For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
# Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        arr = []

        for a, b, c in triplets:
            if a == target[0] or b == target[1] or c == target[2]  :
                arr.append([a,b,c])

        A = B = C = 0

        for a, b, c in arr:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            A, B, C = max(A, a), max(B, b), max(C, c)
            if A == target[0] and B == target[1] and C == target[2]:
                return True
        
        return False
