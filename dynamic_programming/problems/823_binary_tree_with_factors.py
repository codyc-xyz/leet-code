# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9+7
        arr.sort()
        nums = set(n for n in arr)
        numTrees = {x: 1 for x in arr}

        def buildTree(n):
            for c in arr:
                if c > n**0.5:
                    break
                curr = n // c
                if n % c == 0 and curr in nums:
                    if curr == c:
                        numTrees[n] += numTrees[c] * numTrees[c]
                    else:
                        numTrees[n] += numTrees[c] * numTrees[curr] * 2
                    numTrees[n] %= MOD
            return numTrees[n]
        ans = 0
        for n in arr:
            ans += buildTree(n)

        return ans % MOD
