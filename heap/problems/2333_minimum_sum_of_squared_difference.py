# You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

# The sum of squared difference of arrays nums1 and nums2 is defined as the sum of(nums1[i] - nums2[i])2 for each 0 <= i < n.

# You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by + 1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by + 1 or -1 at most k2 times.

# Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

# Note: You are allowed to modify the array elements to become negative integers.

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:

        N = len(nums1)
        remaining = k1 + k2
        diffs = [abs(nums1[i] - nums2[i]) for i in range(N)]
        if remaining >= sum(diffs):
            return 0
        diffs.sort(reverse=True)
        for i, d in enumerate(diffs):
            if i < N - 1:
                currDiff = abs(diffs[i + 1] - diffs[i])
                if currDiff * (i + 1) <= remaining:
                    for j in range(i + 1):
                        if currDiff > remaining:
                            break
                        diffs[j] -= currDiff
                        remaining -= currDiff
                else:
                    currDiff = max(remaining // (i + 1), 1)
                    for j in range(i + 1):
                        if not remaining:
                            break
                        diffs[j] -= currDiff
                        remaining -= currDiff
                    if remaining:
                        for j in range(i + 1):
                            if not remaining:
                                break
                            diffs[j] -= 1
                            remaining -= 1
            else:
                currDiff = max(remaining // (i + 1), 1)
                for j in range(i + 1):
                    if not remaining or currDiff > remaining:
                        break
                    diffs[j] -= currDiff
                    remaining -= currDiff
                if remaining:
                    for j in range(i + 1):
                        if not remaining:
                            break
                        diffs[j] -= 1
                        remaining -= 1

            if not remaining:
                break
        return sum(d**2 for d in diffs)


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:

        N = len(nums1)
        remaining = k1 + k2
        diffs = [abs(nums1[i] - nums2[i]) for i in range(N)]
        if remaining >= sum(diffs):
            return 0
        if remaining == 0:
            return sum(d**2 for d in diffs)

        diffDict = defaultdict(int)

        for n in diffs:
            diffDict[n] += 1

        maxK = max(diffDict.keys())

        for i in range(maxK, -1, -1):
            if diffDict[i] > 0:
                tmp = min(remaining, diffDict[i])
                diffDict[i] -= tmp
                diffDict[i - 1] += tmp
                remaining -= tmp

        ans = 0

        for d in diffDict:
            ans += d ** 2 * diffDict[d]

        return ans
